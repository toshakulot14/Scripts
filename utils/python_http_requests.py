# Simple HTTP Request

import requests

# Place url here
url_to_get=""

# Place appropriate headers here
headers_to_add={"Origin":"asd.com"}

resp=requests.get(url_to_get, headers=headers_to_add)

# Do/process the response 
print(resp.content)
