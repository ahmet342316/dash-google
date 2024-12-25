from flask import Blueprint, request, jsonify
from ..services.trends_service import TrendsService

trends_bp = Blueprint('trends', __name__)
trends_service = TrendsService()

@trends_bp.route('/trends', methods=['POST'])
def get_trends():
    try:
        data = request.json
        timeframe = f"{data['start_date']} {data['end_date']}"
        
        result = trends_service.get_trends_data(
            keywords=data['keywords'],
            timeframe=timeframe,
            geo=data.get('country', 'US')
        )
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500