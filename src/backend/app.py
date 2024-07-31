from flask import Flask
from blueprints.bins_api import bins_api
from blueprints.weather_api import weather_api

app = Flask(__name__)

app.register_blueprint(bins_api, url_prefix='/api/bins')
app.register_blueprint(weather_api, url_prefix='/api/weather')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)