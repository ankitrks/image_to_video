# management/commands/create_superuser.py

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Create a superuser if one does not exist'

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(is_superuser=True).exists():
            username = 'admin'
            email = 'admin@example.com'
            password = 'adminpassword'
            print(f'Creating superuser with username: {username}, email: {email}')
            User.objects.create_superuser(username=username, email=email, password=password)
        else:
            print('Superuser already exists')

