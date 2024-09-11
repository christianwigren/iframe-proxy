from flask import Flask, request, jsonify
import requests

app = Flask(__name__, static_folder=None)


# The target server to forward requests to (base URL)
# TARGET_SERVER = "https://oneflow.legly.io" # does not work for now due to login at our end.
TARGET_SERVER = "https://www.sunet.se" # just for test


# Authentication function to check if the request is authorized
def authenticate_request():
    jwt = True
    # jwt = request.headers.get('oneflow login-jwt or cookie')
    # oneflow validate jwt

    if jwt:
        return True
    return False


# A function to forward the request to the target server
def forward_request(path):
    # Extract the full target URL
    target_url = f"{TARGET_SERVER}/{path}"
    
    # Forward all headers except host (optional, since host would be different for the target server)
    headers = {key: value for key, value in request.headers if key.lower() != 'host'}
    
    # ToDo: Add api_key for oneflow server to authenticate on legly

    # Forward all cookies
    cookies = request.cookies

    # Forward the request based on the method
    if request.method == 'GET':
        response = requests.get(target_url, params=request.args, headers=headers, cookies=cookies)
    elif request.method == 'POST':
        response = requests.post(target_url, json=request.json, headers=headers, cookies=cookies)
    elif request.method == 'PUT':
        response = requests.put(target_url, json=request.json, headers=headers, cookies=cookies)
    elif request.method == 'DELETE':
        response = requests.delete(target_url, headers=headers, cookies=cookies)
    else:
        return jsonify({"error": "Method not allowed"}), 405
    
    # Return the response content, status code, and headers
    return (response.content, response.status_code, response.headers.items())



@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):

    if not authenticate_request():
        return jsonify({"error": "Unauthorized"}), 401

    # Forward the request to the target server
    return forward_request(path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5500)
