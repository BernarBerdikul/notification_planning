from typing import Any

import requests
from config.settings import NOTIFICATION_SERVICE_URL
from notification.schemas import BodyModel

__all__ = ('send_notify',)


def send_notify(path: str, data: dict[str, Any]) -> None:
    """Сериализуем данные и отправляем в сервис notifier."""
    message_body: BodyModel = BodyModel(**data)
    response = requests.post(
        url=f'{NOTIFICATION_SERVICE_URL}{path}',
        data=message_body.json(),
    )
    print(response.json())
