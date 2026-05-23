import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'awning.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Your brand new admin credentials
username = "bigbossadmin"
password = "YourSecurePassword123!" 

if not User.objects.filter(username=username).exists():
    print("Creating live superuser account...")
    User.objects.create_superuser(username=username, email="", password=password)
    print("Superuser created successfully!")
else:
    print("Superuser already exists.")