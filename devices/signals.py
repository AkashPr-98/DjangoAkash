from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from requests import request
from devices.views import testo

@receiver(post_migrate)
def on_server_start(sender, **kwargs):
    if sender.name == 'devices':  # Replace 'myapp' with the actual name of your app
        from .views import testo
        testo(request)