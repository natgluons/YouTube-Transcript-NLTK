from oauth2client import client
import json

# Define the client configuration from the provided JSON
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

# Create a Flow object from the client configuration
flow = client.OAuth2WebServerFlow(
    client_id=client_config["installed"]["client_id"],
    client_secret=client_config["installed"]["client_secret"],
    scope="https://www.googleapis.com/auth/youtube.readonly",
    redirect_uri=client_config["installed"]["redirect_uris"][0],
    response_type="code"  # Add the response_type parameter here
)

# Generate the authorization URL
auth_url = flow.step1_get_authorize_url()

# Print the authorization URL and visit it in your web browser to obtain the access token
print("Authorization URL:", auth_url)