from flask import Flask, request, jsonify
from flask_cors import CORS
from pytrends.request import TrendReq
import pandas as pd
from datetime import datetime

app = Flask(__name__)
CORS(app)

def get_trends_data(keywords, timeframe, geo='US'):
    try:
        pytrends = TrendReq(hl='en-US', tz=360)
        pytrends.build_payload(
            keywords.split(','),
            timeframe=timeframe,
            geo=geo if geo != 'global' else ''
        )
        
        trend_data = pytrends.interest_over_time()
        
        if trend_data.empty:
            return []
            
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

@app.route('/trends', methods=['POST'])
def trends():
    try:
        data = request.json
        timeframe = f"{data['start_date']} {data['end_date']}"
        
        result = get_trends_data(
            keywords=data['keywords'],
            timeframe=timeframe,
            geo=data.get('country', 'US')
        )
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=8050, debug=True)