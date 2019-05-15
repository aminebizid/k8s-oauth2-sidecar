import os
from flask import Flask, request
from urllib.parse import urlparse

app = Flask(__name__)

@app.route("/")
def root():
  return request.headers.environ['HTTP_SIDECAR_CLIENT']

@app.route("/hello")
def hello():
  return 'hello'

if __name__ == "__main__":
     app.run(host='0.0.0.0', port=8090)