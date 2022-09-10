from urllib.request import Request
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User 
from django.dispatch import receiver

@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print('____')
    print('Logged-in Signal.. Run Intro')
    ip = request.META.get('REMOTE_ADDR')
    print('Client_ip', ip)
    request.session['ip'] = ip


