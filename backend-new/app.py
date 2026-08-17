import requests
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

SEARCH_PLAYER_API_URL = 'https://search.d3.nhle.com/api/v1/search/player?culture=en-us&limit=20&q='
PLAYER_CARD_API_URL = 'https://api-web.nhle.com/v1/player/${id}/landing'


@app.route('/search', methods=['GET'])
def search_player_api():
    query = request.args.get('q')
    if not query:
        return jsonify({'error': 'Missing query parameter q'}), 400

    url = SEARCH_PLAYER_API_URL + query

    response = requests.get(url, timeout=10)
    response.raise_for_status()
    raw = response.json()

    if isinstance(raw, dict):
        items = raw.get('data', []) if isinstance(raw.get('data', []), list) else []
    elif isinstance(raw, list):
        items = raw
    else:
        items = []

    players = []
    for item in items:
        if not isinstance(item, dict):
            continue

        player_id = item.get('playerId') or item.get('id')
        name = item.get('name') or item.get('fullName')
        if player_id and name:
            players.append({
                'playerId': player_id,
                'name': name,
            })

    return jsonify(players)


@app.route('/player-card', methods=['GET'])
def player_card_api():
    player_id = request.args.get('id')
    if not player_id:
        return jsonify({'error': 'Missing query parameter id'}), 400

    url = f'https://api-web.nhle.com/v1/player/{player_id}/landing'

    response = requests.get(url, timeout=10)
    response.raise_for_status()
    normalized_data = normalize_default_values(response.json())
    processed_data = processdata(normalized_data)

    return jsonify(processed_data)


def normalize_default_values(value):
    if isinstance(value, dict):
        if 'default' in value and all(
            isinstance(v, (str, int, float, type(None))) for v in value.values()
        ):
            return normalize_default_values(value['default'])
        return {k: normalize_default_values(v) for k, v in value.items()}
    if isinstance(value, list):
        return [normalize_default_values(v) for v in value]
    return value


def processdata(data):
    if not isinstance(data, dict):
        return {}

    return {
        'firstName': data.get('firstName', ''),
        'lastName': data.get('lastName', ''),
        'headshot': data.get('headshot', {}),
        'heroImage': data.get('heroImage', {}),
        'birthDate': data.get('birthDate', ''),
        'birthStateProvince': data.get('birthStateProvince', ''),
        'heightInInches': data.get('heightInInches'),
        'weightInPounds': data.get('weightInPounds'),
        'shootsCatches': data.get('shootsCatches', ''),
        'position': data.get('position', ''),
        'currentTeamAbbrev': data.get('currentTeamAbbrev', ''),
        'sweaterNumber': data.get('sweaterNumber'),
        'birthCity': data.get('birthCity', ''),
        'birthCountry': data.get('birthCountry', ''),
        'seasonTotals': data.get('seasonTotals', {}),
        'careerTotals': data.get('careerTotals', {}),
    }

if __name__== '__main__':
    app.run(debug=True)