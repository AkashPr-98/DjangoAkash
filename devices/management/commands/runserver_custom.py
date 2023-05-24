from django.core.management.base import BaseCommand
from requests import request
from devices.views import testo


class Command(BaseCommand):
    help = 'Starts the development server and calls a function.'

    def handle(self, *args, **options):
        # Call your function here
        testo(request)
        # Additional initialization or startup code if needed