import requests
response = requests.post('http://127.0.0.1:8000/api/students/',data={'name':'Shuhrat'})
print(response.status_code)