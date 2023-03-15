from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    target_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    source_currency = data['queryResult']['parameters']['currency-name']

    final_amount = fetch_conversion_factor(source_currency, target_currency, amount)

    response = {
        'fulfillmentText': "{} {} is {} {}".format(amount, target_currency, final_amount, source_currency)
    }
    return jsonify(response)


def fetch_conversion_factor(source, target, amount):
    url = "https://api.apilayer.com/exchangerates_data/convert?to={}&from={}&amount={}&apikey=aiYgCur2Ov0iuNAgwihsTx3NsFoCxwip".format(
        source, target, amount)
    response = requests.get(url)
    response = response.json()
    return response['result']


if __name__ == "__main__":
    app.run(debug=True)
