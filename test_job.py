from requests import get, post, delete

print(get('http://localhost:5000/api/v2/jobs').json())
print(get('http://localhost:5000/api/v2/jobs/1').json())
print(get('http://localhost:5000/api/v2/jobs/999').json())

print(post('http://localhost:5000/api/v2/jobs',
           json={'team_leader': '1',
                 'job': 'govorit intEger vmesto integer',
                 'work_size': 30,
                 'collaborators': '2, 3',
                 'is_finished': False}).json())

print(get('http://localhost:5000/api/v2/jobs/7').json())

print(delete('http://localhost:5000/api/v2/jobs/7').json())

print(get('http://localhost:5000/api/v2/jobs/7').json())
