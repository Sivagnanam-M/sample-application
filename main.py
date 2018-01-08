from flask import Flask
import requests



app = Flask(__name__)


def home():
    req = requests.get('https://s3.amazonaws.com/cloneexport/Ap24168f58_3337_11e5_9424_22000ab34466/sysapplication.csv')
    return req.text 

app.add_url_rule(rule='/', endpoint='home', view_func=home, methods=['GET'])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)