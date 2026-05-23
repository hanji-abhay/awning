import os
from django.apps import AppConfig

class WebsiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'website'

    def ready(self):
        # This code runs EXACTLY once as soon as Django is fully loaded and safe
        # We check for a specific environment variable so it only runs on Render live, not your local machine!
        if os.environ.get('DATABASE_URL'):
            try:
                from django.contrib.auth import get_user_model
                User = get_user_model()
                
                username = "bigbossadmin"
                password = "YourSecurePassword123!"
                
                if not User.objects.filter(username=username).exists():
                    print("RENDER SETUP: Creating live superuser account...")
                    User.objects.create_superuser(username=username, email="", password=password)
                    print("RENDER SETUP: Superuser created successfully!")
                else:
                    print("RENDER SETUP: Superuser already exists.")
            except Exception as e:
                # Catch errors gracefully so the build never crashes again
                print(f"RENDER SETUP: Admin creation skipped: {e}")