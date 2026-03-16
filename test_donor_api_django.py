import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.test import Client

client = Client()

# TEST 1: Register Donor
donor_payload = {
    'name': 'Test User',
    'blood_group': 'A+',
    'phone': '+918888888999',
    'email': 'test@udaansociety.org',
    'city': 'Test City',
    'state': 'Test State',
    'pin_code': '110001',
    'consent_given': True,
    'whatsapp_number': '1234567890',
    'email_notifications': True,
    'available_to_donate': True
}

print("Testing /api/register/...")
res1 = client.post('/api/register/', data=json.dumps(donor_payload), content_type='application/json')
print(f"Status: {res1.status_code}")
print(f"Response: {res1.content.decode()}")

# TEST 2: Submit Blood Request
request_payload = {
    'patient_name': 'Test Patient',
    'blood_group': 'A+',
    'hospital_name': 'Test Hospital',
    'contact_phone': '+918888888111',
    'contact_person': 'Test Patient',
    'city': 'Test City',
    'state': 'Test State',
    'pin_code': '110001',
    'is_emergency': True
}

print("\nTesting /api/blood-request/...")
res2 = client.post('/api/blood-request/', data=json.dumps(request_payload), content_type='application/json')
print(f"Status: {res2.status_code}")
print(f"Response: {res2.content.decode()}")
