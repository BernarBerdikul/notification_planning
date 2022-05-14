import logging
from typing import Any

from celery import shared_task

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
    for email, rendered_subject, rendered_body in mail_generator.weekly_top_movies(
            email_template,
    ):
        data: dict[str, Any] = {
            'recipient': email,
            'subject': rendered_subject,
            'body': rendered_body,
        }
        send_notify(data=data)
