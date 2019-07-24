
import requests

url = "https://hao.360.com/"

querystring = {"360safe":""}

payload = ""
headers = {
    'cache-control': "no-cache",
    'Postman-Token': "ecb3949f-9786-4d0a-b2cd-c2b855fedbbb"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)