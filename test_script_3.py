import requests

url = 'http://127.0.0.1:8000/get_form/'
data = {
  "name": "street",
  "may": "01.01.2000",
  "oil": "2024-12-09"
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())


# application/x-www-form-urlencoded
# name=street&may=01.01.2000&oil=2024-12-09
