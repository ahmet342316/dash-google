import time
from datetime import datetime
from pytrends.request import TrendReq
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from config import MAX_RETRIES, RETRY_DELAY, TIMEOUT

class TrendsAPI:
    def __init__(self):
        self.session = self._create_session()
        self.pytrends = None
        self._initialize_pytrends()

    def _create_session(self):
        session = requests.Session()
        retry_strategy = Retry(
            total=MAX_RETRIES,
            backoff_factor=0.5,
            status_forcelist=[500, 502, 503, 504],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("https://", adapter)
        session.mount("http://", adapter)
        return session

    def _initialize_pytrends(self):
        try:
            self.pytrends = TrendReq(
                hl='en-US',
                tz=360,
                timeout=TIMEOUT,
                requests_args={'verify': True}
            )
        except Exception as e:
            print(f"Failed to initialize pytrends: {e}")
            raise

    def get_trends_data(self, keywords, timeframe, geo):
        if not self.pytrends:
            self._initialize_pytrends()

        try:
            keywords_list = [kw.strip() for kw in keywords.split(',')]
            
            # Handle global search
            if geo == 'global':
                geo = ''
                
            self.pytrends.build_payload(keywords_list, timeframe=timeframe, geo=geo)
            time.sleep(RETRY_DELAY)  # Prevent rate limiting
            
            data = self.pytrends.interest_over_time()
            
            if data.empty and geo == '':
                # Try individual countries if global data is empty
                return self._get_country_specific_data(keywords_list, timeframe)
                
            return data, None
            
        except Exception as e:
            return None, str(e)

    def _get_country_specific_data(self, keywords_list, timeframe):
        combined_data = None
        for geo in ['US', 'GB', 'AU', 'IN']:
            try:
                self.pytrends.build_payload(keywords_list, timeframe=timeframe, geo=geo)
                time.sleep(RETRY_DELAY)
                data = self.pytrends.interest_over_time()
                
                if not data.empty:
                    # Rename columns to include country code
                    data.columns = [f"{col} ({geo})" for col in data.columns 
                                  if col != 'isPartial']
                    
                    if combined_data is None:
                        combined_data = data
                    else:
                        combined_data = combined_data.join(
                            data.drop('isPartial', axis=1, errors='ignore')
                        )
            except Exception:
                continue

        return combined_data, None