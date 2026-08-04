import requests
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

SEARCH_PLAYER_API_URL = 'https://search.d3.nhle.com/api/v1/search/player?culture=en-us&limit=20&q='


@app.route('/search', methods=['GET'])
def search_player_api():
    query = request.args.get('q', 'sidney')
    url = SEARCH_PLAYER_API_URL + query

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return jsonify(response.json())


if __name__== '__main__':
    app.run()