from os import path, environ
from sys import path as sys_path
from django import setup

sys_path.append("/config/settings.py")
environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
setup()
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
from notification.mail_generator import DummyMailGenerator
import requests

log = logging.getLogger(__name__)


@shared_task
def friday_top():
    """Задача для отправки топа фильмов недели."""
    template = EmailTemplate.objects.filter(mail_type="welcome_letter").first()
    gen_mail = DummyMailGenerator(template)
    for recipient, html in gen_mail.personal_film_selection():
        body = {
                "recipient": recipient,
                "subject": template.subject,
                "body": html,
                "immediately": False,
                "log_it": True,
                "ttl": 60*60*6
                }
        requests.post("127.0.0.1", json=body)

@shared_task
def new_movies():
    """Задача для отправки топа фильмов недели."""
    template = EmailTemplate.objects.filter(mail_type="welcome_letter").first()
    gen_mail = DummyMailGenerator(template)
    for recipient, html in gen_mail.latest_new_movies():
        body = {
                "recipient": recipient,
                "subject": template.subject,
                "body": html,
                "immediately": False,
                "log_it": True,
                "ttl": 60*60*6
                }
        requests.post("127.0.0.1", json=body)

@shared_task
def new_movies():
    """Задача для отправки топа фильмов недели."""
    template = EmailTemplate.objects.filter(mail_type="welcome_letter").first()
    gen_mail = DummyMailGenerator(template)
    for recipient, html in gen_mail.latest_new_movies():
        body = {
                "recipient": recipient,
                "subject": template.subject,
                "body": html,
                "immediately": False,
                "log_it": True,
                "ttl": 60*60*6
                }
        requests.post("тут_адрес_приложения_Кости", json=body)

