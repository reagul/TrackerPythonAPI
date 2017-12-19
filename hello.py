
from flask import Flask
import os
from flask import jsonify
import requests 

app = Flask(__name__)

TOKEN = '3f8f2d63167a1718ea6e3c7036842e65'
port = int(os.getenv("PORT"))

@app.route('/author')
def hello_world():
    return jsonify(
        username='Ravi Jagannathan',
        email='rjagannathan@pivotal.io'
        )
@app.route('/')
def api():
    return jsonify(
        version='1.0.0'
    )

# TODO Handle requests.exceptions.ConnectionError

@app.route('/projects')
def _perform_pivotal_get():
    headers = {'X-TrackerToken': TOKEN}
    url = 'https://www.pivotaltracker.com/services/v5/projects'
    print url
    
    response = requests.get(url, headers=headers)
    print "@@@@@@@@@@@@@@ PROJECTS @@@@@@@@@@@@@@@"
    #print response.content
    return jsonify(response.content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)