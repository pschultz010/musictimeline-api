from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    return jsonify({'res': 'ok'})

@app.route('/followedartists', methods = ['GET'])
def user():
    headers = {'Authorization': 'Bearer '+request.headers['X-Spotify-Token']}
    r = requests.get('https://api.spotify.com/v1/me/following?type=artist', headers=headers).json()

    return jsonify({'artists': [r['name'] for r in r['artists']['items']]})
