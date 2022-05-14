from typing import Any

import requests
from config.settings import NOTIFICATION_SERVICE_URL
from notification.schemas import EmailBodyModel

__all__ = ('send_notify',)


def send_notify(data: dict[str, Any]) -> None:
    """Сериализуем данные и отправляем в сервис notifier."""
    email_body: EmailBodyModel = EmailBodyModel(**data)

    response = requests.post(
        url=f'{NOTIFICATION_SERVICE_URL}/api/v1/send/email/',
        data=email_body.json(),
    )
    print(response.json())
