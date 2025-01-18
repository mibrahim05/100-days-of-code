import requests
from datetime import datetime
user_name =""
TOKEN = ""
GRAPH_ID =""
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":TOKEN,
    "username":user_name,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{user_name}/graphs"

graph_config = {
    "id":GRAPH_ID,
    "name":"Coding graph",
    "unit":"Hr",
    "type":"int",
    "color":"sora"
}

headers = {
    "X-USER-TOKEN":TOKEN,
}
#
# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

pixel_creation = f"{pixela_endpoint}/{user_name}/graphs/{GRAPH_ID}"
today = datetime.now()
# print(today.strftime("%Y%m%d"))
pixel_data = {
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many Hours did you Code Today?"),
}
#
response = requests.post(url=pixel_creation,json=pixel_data,headers=headers)
print(response.text)
pixel_update = f"{pixela_endpoint}/{user_name}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
pixel_up = {
    "quantity":"7"
}
# response = requests.put(url=pixel_update,json=pixel_up,headers=headers)
# print(response.text)

# delete_endpoint = f"{pixela_endpoint}/{user_name}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# pixel_del = requests.delete(url=delete_endpoint,headers=headers)
# print(pixel_del.text)
