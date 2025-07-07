import requests
from flask import request, Response, jsonify

def register_routes(app):

    @app.route('/', methods=['GET'])
    def welcome():
        return jsonify({"message": "Welcome to Smartflo Proxy API"}), 200

    @app.route('/smartflo/support_call', methods=['POST'])
    def support_call():
        data = request.get_json()

        if not data:
            return jsonify({"error": "Missing JSON body"}), 400

        api_key = data.get('api_key')
        customer_number = data.get('customer_number')

        if not api_key or not customer_number:
            return jsonify({"error": "Missing required fields: api_key, customer_number"}), 400

        url = "https://api-smartflo.tatateleservices.com/v1/click_to_call_support"
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        payload = {
            "api_key": api_key,
            "customer_number": customer_number
        }

        resp = requests.post(url, json=payload, headers=headers)

        return Response(resp.content, status=resp.status_code, content_type='application/json')
