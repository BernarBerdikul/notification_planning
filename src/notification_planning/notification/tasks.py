# import json
import logging

# from datetime import datetime
from typing import Any

from celery import shared_task
from django.conf import settings
from notification.models import EmailTemplate
from notification.services import DummyMailGenerator, send_notify

log = logging.getLogger(__name__)

mail_generator = DummyMailGenerator()


@shared_task
def friday_top():
    """Задача для отправки топа фильмов недели."""
    email_template: EmailTemplate = EmailTemplate.objects.filter(
        mail_type='selection_movies',
    ).first()
    for user, rendered_subject, rendered_body in \
            settings.mail_generator.weekly_top_movies(email_template):
        data: dict[str, Any] = {
            'recipient': user.email,
            'subject': rendered_subject,
            'body': rendered_body,
        }
        send_notify(data=data)


# @shared_task
# def selections_movies_for_user():
#     """Задача для созднания уведомлений."""
#     # find users
#     users = []
#     for user in users:
#         # find movies
#         movies = []
#         create_msg = format_email_body(user, movies)
#         send_notification = send()


@shared_task
def send_notification():
    """Задача на отправку уведомлений менеджерам."""
    b = 10
    print(b)
