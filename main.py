from flask import Flask
import requests



app = Flask(__name__)


def home():
    return "message is ok"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)