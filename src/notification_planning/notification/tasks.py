# import json
import logging
# from datetime import datetime

from celery import shared_task, states
# from django.conf import settings
# from django.contrib.auth.models import User
# from django.core.mail import send_mail
# from django_celery_results.models import TaskResult
#
from notification.models import EmailTemplate
from notification.utils import format_email_body

log = logging.getLogger(__name__)

def plugin(*args):
    return [("1@m.ru", "1"),("3@m.ru", "3"),("5@m.ru", "5")]

# @shared_task
# def welcome_msg_to_user():
#     """Задача для созднания приветственного уведомления."""
#     template = EmailTemplate.objects.filter(mail_type="welcome_letter")
#     users = plugin("welcome_letter")
#     for user in users:
#         create_msg = format_email_body(user, movies)
#         send_notification = send()
#
#
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

