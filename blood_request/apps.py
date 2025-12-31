from django.apps import AppConfig


class BloodRequestConfig(AppConfig):
    name = "blood_request"

    def ready(self):
        # Auto-migrate for in-memory database stability
        from django.conf import settings
        import sys
        
        # Only start migration if it's an in-memory DB and we are running the server
        if settings.DATABASES['default']['NAME'] == ':memory:' and 'runserver' in sys.argv:
            from django.core.management import call_command
            try:
                # We can't use interactive=False here easily because it might output to stdout
                # but we can try to wrap it.
                call_command('migrate', interactive=False)
            except Exception:
                pass
