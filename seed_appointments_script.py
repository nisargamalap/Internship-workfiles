import os
import django
import random
from datetime import timedelta
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.contrib.auth.models import User
from blood_request.models import Appointment

def run():
    print("Seeding appointments...")
    staff_users = User.objects.filter(is_staff=False, is_superuser=False)
    
    if not staff_users.exists():
        print("No staff users found. Creating 'staff1'...")
        try:
            staff1 = User.objects.create_user('staff1', 'staff1@example.com', 'password123')
            staff_users = [staff1]
        except Exception as e:
            # If user exists but filter missed it (e.g. they are staff=True), fetch staff1 specifically
            print(f"Error creating user (might exist): {e}")
            try:
                staff_users = [User.objects.get(username='staff1')]
            except:
                print("Could not find or create staff1.")
                return

    titles = [
        "Donor Follow-up: John Doe",
        "Site Visit: Aligarh Center",
        "Team Sync: Weekly",
        "Equipment Check",
        "Camp Planning Meeting"
    ]
    
    statuses = ['Scheduled', 'Completed', 'Cancelled']
    
    count = 0
    for user in staff_users:
        for _ in range(3):
            base_time = timezone.now() + timedelta(days=random.randint(-2, 5))
            Appointment.objects.create(
                title=random.choice(titles),
                description="This is a demo appointment generated for testing.",
                start_time=base_time,
                end_time=base_time + timedelta(hours=1),
                staff=user,
                status=random.choice(statuses)
            )
            count += 1
    
    print(f"Successfully created {count} demo appointments.")

if __name__ == '__main__':
    run()
