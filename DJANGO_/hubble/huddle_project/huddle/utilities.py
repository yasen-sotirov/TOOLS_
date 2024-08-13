from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
from .models import Item
from datetime import timedelta



def notify_users(huddle, user):
    users = []

    for item in huddle.items.all():
        if item.user not in users:
            users.append(item.user)

    subject = f'New message in {huddle.key}'
    message = f'{user} wrote a new message'
    form_email = settings.DEFAULT_FROM_EMAIL

    send_mail(subject, message, form_email, users)




def remove_old_huddles():
    twenty_four_hours_ago = timezone.now() - timedelta(hours=24)
    old_items = Item.objects.filter(created_at__gt = twenty_four_hours_ago)