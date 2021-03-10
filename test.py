from requests import get, post, delete, put

#  print(get('http://localhost:5000/api/jobs').json())
#  print(get('http://localhost:5000/api/jobs/1').json())
#
#  print(get('http://localhost:5000/api/jobs/999').json())
#  print(get('http://localhost:5000/api/jobs/q').json())
#  print(post('http://localhost:5000/api/jobs').json())
#
#  print(post('http://localhost:5000/api/jobs',
#             json={'team_leader': 1}).json())
#
#  print(get('http://localhost:5000/api/jobs').json())
#
#  print(post('http://localhost:5000/api/jobs',
#             json={'id': 666,
#                   'team_leader': 1,
#                   'job': 'Привет всем я лёха',
#                   'work_size': 45,
#                   'collaborators': '2, 3',
#                   'is_finished': False}).json())
#
print(get('http://localhost:5000/api/jobs/7').json())
print(put('http://localhost:5000/api/jobs',
          json={'id': 7,
                'team_leader': 2,
                'job': 'development'}).json())
print(get('http://localhost:5000/api/jobs/7').json())

print(put('http://localhost:5000/api/jobs',
          json={'id': 'eeeded',
                'team_leader': 2,
                'job': 'Привет всем я sanya'}).json())


print(get('http://localhost:5000/api/jobs').json())
#  print(delete('http://localhost:5000/api/jobs/ee').json())
#  print(delete('http://localhost:5000/api/jobs/1999').json())
