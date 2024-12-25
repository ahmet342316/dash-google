from pytrends.request import TrendReq
from datetime import datetime
from ..config import Config

class TrendsService:
    def __init__(self):
        self.pytrends = TrendReq(
            hl=Config.DEFAULT_LANGUAGE,
            tz=Config.DEFAULT_TIMEZONE
        )

    def get_trends_data(self, keywords, timeframe, geo=Config.DEFAULT_COUNTRY):
        try:
            # Build payload
            self.pytrends.build_payload(
                keywords.split(','),
                timeframe=timeframe,
                geo=geo if geo != 'global' else ''
            )
            
            # Get interest over time
            trend_data = self.pytrends.interest_over_time()
            
            if trend_data.empty:
                return []
                
            # Convert to format suitable for Recharts
            result = []
            for index, row in trend_data.iterrows():
                data_point = {'date': index.strftime('%Y-%m-%d')}
                for column in trend_data.columns:
                    if column != 'isPartial':
                        data_point[column] = float(row[column])
                result.append(data_point)
                
            return result
            
        except Exception as e:
            raise Exception(f"Failed to fetch trends data: {str(e)}")