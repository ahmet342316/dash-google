from datetime import datetime

# App configuration
DEFAULT_KEYWORDS = 'recession,stock market'
DEFAULT_START_DATE = "2004-01-01"
DEFAULT_END_DATE = datetime.today().strftime('%Y-%m-%d')

# API configuration
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds
TIMEOUT = 30  # seconds

# Countries for the dropdown
COUNTRIES = [
    {'label': 'United States', 'value': 'US'},
    {'label': 'United Kingdom', 'value': 'GB'},
    {'label': 'Australia', 'value': 'AU'},
    {'label': 'India', 'value': 'IN'},
    {'label': 'Global', 'value': 'global'}
]