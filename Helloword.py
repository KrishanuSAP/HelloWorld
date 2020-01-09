import requests as reqs

for i in range(1, 2):
    print('Welcome to RE')

response = reqs.get('https://www.google.com')
print(response.status_code)
