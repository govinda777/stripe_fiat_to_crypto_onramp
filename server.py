#! /usr/bin/env python3.6
"""
Python 3.6 or newer required.
"""
import json
import os
import stripe

# This is a public sample test API key.
# Don’t submit any personally identifiable information in requests made with this key.
# Sign in to see your own test API key embedded in code samples. .env 
stripe.api_key = os.getenv('STRIPE_PRIVATE_API_KEY')

from flask import Flask, render_template, jsonify, request


app = Flask(__name__, static_folder='public',
            static_url_path='', template_folder='public')

@app.route('/create-onramp-session', methods=['POST'])
def create_payment():
    try:
        data = json.loads(request.data)
        # Create an OnrampSession with the order amount and currency
        onramp_session = stripe.stripe_object.StripeObject().request(
          "post",
          "/v1/crypto/onramp_sessions",
          {
            "transaction_details": {
              "destination_currency": data["transaction_details"]["destination_currency"],
              "destination_exchange_amount": data["transaction_details"]["destination_exchange_amount"],
              "destination_network": data["transaction_details"]["destination_network"],
            },
            "customer_ip_address": request.remote_addr,
          })

        return jsonify({
            'clientSecret': onramp_session['client_secret']
        })
    except Exception as e:
        return jsonify(error=str(e)), 403
if __name__ == '__main__':
    app.run(port=4242)