from flask import Flask
import requests
import random


app = Flask(__name__)


def home():
    n = random.randint(1, 4)
    req = requests.get('https://s3.amazonaws.com/rajesh-test11/%s.json' % n)
    return req.text 

app.add_url_rule(rule='/', endpoint='home', view_func=home, methods=['GET'])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)