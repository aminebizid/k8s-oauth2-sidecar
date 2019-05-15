import os
from flask import request
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from app_base import app
from security.auth import oauth

@oauth.authorize('hello')
@app.before_request
def before_request():
    if request.path == '/signin-oidc':
      return
    host = request.host_url
    targetUrl = request.url.replace(host, os.getenv('target_url'))
    req = Request(targetUrl)
    req.add_header('sidecar_client', oauth.get_client())
    contents = urlopen(req).read()
    return contents

if __name__ == "__main__":
     app.run(host='0.0.0.0', port=5000)