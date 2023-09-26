import requests
import json

# Define the client configuration
client_config = {
    "installed":{
        "client_id":"20745388261-9kr7320a2hillg37vlbsj3d072phjqu6.apps.googleusercontent.com",
        "project_id":"atlantean-theme-400009",
        "auth_uri":"https://accounts.google.com/o/oauth2/auth",
        "token_uri":"https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
        "client_secret":"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",
        "redirect_uris":["http://localhost"]
    }
}

# Define the authorization code
authorization_code = "4/0AfJohXmvi6fL9JBlTT8JxAPsJ7Q98vOZqNU2eLW05Tbqgz2ohyEMOGyZB3tIn4XVYE5bHA"  # Replace with your actual authorization code

# Define the token request data
token_request_data = {
    "code": authorization_code,
    "client_id": client_config["installed"]["client_id"],
    "client_secret": client_config["installed"]["client_secret"],
    "redirect_uri": client_config["installed"]["redirect_uris"][0],
    "grant_type": "authorization_code"
}

# Make a POST request to the token endpoint
token_url = client_config["installed"]["token_uri"]
response = requests.post(token_url, data=token_request_data)

# Check if the request was successful
if response.status_code == 200:
    token_data = response.json()
    access_token = token_data.get("access_token")
    print("Access Token:", access_token)
else:
    print("Failed to obtain access token. Status code:", response.status_code)
    print("Error response:", response.text)