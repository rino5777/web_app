import requests

url = 'http://127.0.0.1:8000/get_form/'  
data = {
  "name": "power",
  "while": "text",
  "occur": "example@school.com",
  "from": "01.01.2000"
}

response = requests.post(url, json=data)  
print(response.status_code)  
print(response.json())  



# application/x-www-form-urlencoded
# name=power&while=text&occur=example@school.com&from=01.01.2000
