import requests
import json

# Define the YouTube Data API endpoint and specify parameters
api_endpoint = "https://www.googleapis.com/youtube/v3/videos"
params = {
    "part": "snippet",   # Specify the parts of the video you want to retrieve
    "myRating": "like",  # Retrieve videos that you have liked (your watch history)
    "maxResults": 10,    # Maximum number of results to retrieve per request
}

# Include the access token in the request headers
headers = {
    "Authorization": "[Replace this with your own access token]}

# Initialize an empty list to store video IDs
watch_history_ids = []

# Make API requests until all watch history is retrieved (pagination)
while True:
    response = requests.get(api_endpoint, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if "items" in data:
            for video in data["items"]:
                watch_history_ids.append(video["id"])
        if "nextPageToken" in data:
            params["pageToken"] = data["nextPageToken"]
        else:
            break
    else:
        print("Error:", response.status_code, response.text)
        break

# Save the video IDs in a JSON file
file_path = r"C:\VS Code\watch_history_ids.json"
with open(file_path, "w") as json_file:
    json.dump(watch_history_ids, json_file, indent=4)

# Print the video IDs from watch history
for video_id in watch_history_ids:
    print(video_id)

print("Video IDs saved to 'watch_history_ids.json'")
