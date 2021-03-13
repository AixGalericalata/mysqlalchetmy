from requests import get, post, delete, put

print(get('http://localhost:5000/api/v2/users').json())
print(get('http://localhost:5000/api/v2/users/1').json())
