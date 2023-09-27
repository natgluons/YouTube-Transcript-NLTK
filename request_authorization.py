from oauth2client import client
import json
import webbrowser  # Import the webbrowser module

def request_authorization(client_config):
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

    # Open the authorization URL in the default web browser
    webbrowser.open(auth_url)

    # Return the authorization URL (optional, you can remove this)
    return auth_url

# Define the client configuration from the provided JSON
client_config = {
    "installed": {
        "client_id": "20745388261-9kr7320a2hillg37vlbsj3d072phjqu6.apps.googleusercontent.com",
        "project_id": "atlantean-theme-400009",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_secret": "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",
        "redirect_uris": ["http://localhost"]
    }
}

# If you want to test the function, you can call it like this:
if __name__ == "__main__":
    auth_url = request_authorization(client_config)
    print("Authorization URL:", auth_url)

# INSTRUCTION
# Click the url, the site will be unaccessible, but the code is in the link
# The link will change to something like: http://localhost:5000/oauth2callback?code=4/0AfJohXmLUdO-Aqq_osPF4r2bGKtI_YQC8tN1hSi4kx2rpNuY_8p0jWSz927Wa_h9yJ1bXg&scope=https://www.googleapis.com/auth/youtube.readonly
# Your code is the one after ?code=
# Your code will look something like: 4/0AfJohXmLUdO-Aqq_osPF4r2bGKtI_YQC8tN1hSi4kx2rpNuY_8p0jWSz927Wa_h9yJ1bXg
