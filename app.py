# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask_restful import Resource, Api
from redis import Redis

app = Flask(__name__)
api = Api(app)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
