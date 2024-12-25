from flask import Flask
from flask_cors import CORS
from .routes.trends_routes import trends_bp
from .config import Config

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Register blueprints
    app.register_blueprint(trends_bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=Config.PORT, debug=Config.DEBUG)