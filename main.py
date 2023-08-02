import requests
import os
from datetime import datetime

USER_NAME = "robertdosek"
TOKEN = os.environ["PIXELA_TOKEN"]
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# # Create user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Create graph
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id" : GRAPH_ID,
    "name": "Walking Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}

# Headers auth
headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Post a pixel
pix_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime.now()

post_pixel = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "18.6",
}

# response = requests.post(url=pix_endpoint, json=pix_config, headers=headers)
# print(response.text)

# Update pixel
pix_update_end_point = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/20230801"

update_pixel = {
    "quantity": "32.0",
}

# response = requests.put(url=pix_update_end_point, json=update_pixel, headers=headers)
# print(response.text)

# Delete pixel
pix_delete_end_point = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/20230801"

response = requests.delete(url=pix_delete_end_point, headers=headers)
print(response.text)