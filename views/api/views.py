from flask import jsonify, request
from . import api

@api.route('/fetch_tweet', methods=['POST'])
def fetch_tweet():
    # Logica per recuperare i tweet
    return jsonify({'status': 'success', 'tweet': tweet_data})

# Altre route API...
