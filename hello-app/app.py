from flask import Flask, request, jsonify
from functools import wraps
import base64

app = Flask(__name__)

# Simple auth middleware
def check_auth(username, password):
    return username == 'admin' and password == 'secret'

def authenticate():
    message = {'message': "Authentication required."}
    resp = jsonify(message)
    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Login Required"'
    return resp

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/hi')
@requires_auth
def hi():
    return 'Hi there, authenticated user!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
