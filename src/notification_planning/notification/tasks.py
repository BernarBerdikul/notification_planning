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
    email  = "aaa"
    html = "<sasda>"
    return [("1@m.ru", "1"),("3@m.ru", "3"),("5@m.ru", "5")]

@shared_task
def friday_top():
    """Задача для отправки топа фильмов недели."""
    template = EmailTemplate.objects.filter(mail_type="welcome_letter").first()
    # all = plugin(template)
    users = abstract_services.get_active_users()
    movies = abstract_services.get_popular_movies()

    for user in users:
        html = render(template.email_text, user, movies)
        body = {
                    "recipient": user.email,
                    "subject": template.subject,
                    "body": html,
                    "immediately": False,
                    "log_it": True,
                    "ttl": 60*60*6
                    }

        send_notification = request.post(endpoint, data=body)


@shared_task
def selections_movies_for_user():
    """Задача для созднания уведомлений."""
    # find users
    users = []
    for user in users:
        # find movies
        movies = []
        create_msg = format_email_body(user, movies)
        send_notification = send()


@shared_task
def send_notification():
    """Задача на отправку уведомлений менеджерам."""
    b = 10
    print(b)

