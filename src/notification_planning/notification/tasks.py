import logging
from typing import Any

from celery import shared_task
from config.settings import NOTIFICATION_SERVICE_PATH_EMAIL as email_path
from config.settings import NOTIFICATION_SERVICE_PATH_WEBPUSH as webpush_path
from config.settings import NOTIFICATION_SERVICE_PATH_WEBSOCKET as websocket_path
from notification.models import MessageTemplate
from notification.services import (  # MailGenerator,
    DummyMailGenerator,
    WebpushGenerator,
    WebsocketGenerator,
    send_notify,
)

log = logging.getLogger(__name__)

# mail_generator = MailGenerator()
mail_generator = DummyMailGenerator()
websocket_generator = WebsocketGenerator()
webpush_generator = WebpushGenerator()


@shared_task
def friday_top_email():
    """Задача для отправки топа фильмов недели по почте."""
    email_template: MessageTemplate = MessageTemplate.objects.filter(
        mail_type='selection_movies', channel='email',
    ).first()
    for email, rendered_subject, rendered_body in mail_generator.weekly_top_movies(
            email_template,
    ):
        data: dict[str, Any] = {
            'recipient': email,
            'subject': rendered_subject,
            'body': rendered_body,
        }
        send_notify(email_path, data)


@shared_task
def friday_top_websocket():
    """Задача для отправки топа фильмов недели через websocket."""
    web_template: MessageTemplate = MessageTemplate.objects.filter(
        mail_type='selection_movies', channel='websocket',
    ).first()
    for recipient, rendered_subject, rendered_body in websocket_generator.weekly_top_movies(
            web_template,
    ):
        data: dict[str, Any] = {
            'recipient': recipient,
            'subject': rendered_subject,
            'body': rendered_body,
        }
        send_notify(websocket_path, data)


@shared_task
def friday_top_webpush():
    """Задача для отправки топа фильмов недели через push уведомление."""
    web_template: MessageTemplate = MessageTemplate.objects.filter(
        mail_type='selection_movies', channel='web_push',
    ).first()
    for recipient, rendered_subject, rendered_body in mail_generator.weekly_top_movies(
            web_template,
    ):
        data: dict[str, Any] = {
            'recipient': recipient,
            'subject': rendered_subject,
            'body': rendered_body,
        }
        send_notify(webpush_path, data)
