from requests import get, post

print(get('http://localhost:5000/api/jobs').json())
print(get('http://localhost:5000/api/jobs/1').json())

print(get('http://localhost:5000/api/jobs/999').json())
print(get('http://localhost:5000/api/jobs/q').json())
print(post('http://localhost:5000/api/jobs').json())

print(post('http://localhost:5000/api/jobs',
           json={'team_leader': 1}).json())

print(get('http://localhost:5000/api/jobs').json())


print(post('http://localhost:5000/api/jobs',
           json={'team_leader': 1,
                 'job': 'Привет всем я лёха',
                 'work_size': 45,
                 'collaborators': '2, 3',
                 'is_finished': False}).json())
