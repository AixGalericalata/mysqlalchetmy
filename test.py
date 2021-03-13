from requests import get, post, delete

print(get('http://localhost:5000/api/v2/users').json())
print(get('http://localhost:5000/api/v2/users/1').json())
print(get('http://localhost:5000/api/v2/users/999').json())

print(post('http://localhost:5000/api/v2/users',
           json={'surname': 'Dima',
                 'name': 'Ivanov',
                 'age': 45,
                 'position': 'e5',
                 'speciality': 'Dydya',
                 'address': 'ulica_puskina',
                 'email': 'hehe@mail.ru',
                 'hashed_password': 'odnosroronyafunction-hren'}).json())

print(get('http://localhost:5000/api/v2/users/7').json())

print(delete('http://localhost:5000/api/v2/users/7').json())

print(get('http://localhost:5000/api/v2/users/7').json())
