import requests

url = 'http://127.0.0.1:8000/get_form/'
data = {
  "name": "pressure",
  "with": "text",
  "improve": "01.01.2000",
  "beautiful": "+7 123 456 78 90"
}


response = requests.post(url, json=data)
print(response.status_code)
print(response.json())




# application/x-www-form-urlencoded
# name=pressure&with=text&improve=01.01.2000&beautiful=+7 123 456 78 90
