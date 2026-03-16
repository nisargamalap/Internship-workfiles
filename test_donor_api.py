import urllib.request
import json

url = 'http://localhost:8000/api/register/'
payload = {
    'name': 'Test User',
    'blood_group': 'A+',
    'phone': '+918888888321', # unique
    'email': 'test@udaansociety.org',
    'city': 'Test City',
    'state': 'Test State',
    'pin_code': '110001',
    'consent_given': True,
    'whatsapp_number': '1234567890',
    'email_notifications': True,
    'available_to_donate': True
}

req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json'})
try:
    with urllib.request.urlopen(req) as response:
        print(f'Status Code: {response.status}')
        print(f'Response: {response.read().decode("utf-8")}')
except Exception as e:
    print(f'Error: {e}')
