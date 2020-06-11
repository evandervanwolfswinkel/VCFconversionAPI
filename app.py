# app.py - a minimal flask api using flask_restful
import codecs
import csv
import flask
from flask import Flask, render_template, request, url_for, jsonify
from flask_restful import Resource, Api
from redis import Redis
import searchVariants

app = Flask(__name__)
api = Api(app)
redis = Redis(host='redis', port=6379)

# Author: Evander van Wolfswinkel & Rick Schoenmaker
# FLASK REST API, contains routing of urls to file requesting POST method


# Route to send POST request using
# 'curl -H "Content-Type: multipart/form-data" -F "file=@testinput.csv" http://localhost:5000/upload'
@app.route('/upload', methods=['POST'])
def upload():
    flask_file = request.files['file'] # Request file when one is given
    if not flask_file:
        return 'Upload a CSV file'
    data = []
    stream = codecs.iterdecode(flask_file.stream, 'utf-8')
    for row in csv.reader(stream, dialect=csv.excel):
        if row:
            data.append(row)
    results = searchVariants.main(data) # Search data stream for variants
    return jsonify(results) # Return JSON of results

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
