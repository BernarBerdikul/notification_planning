from typing import Optional

from config import settings
from notification.schemas import FastJsonModel

__all__ = ('BodyModel',)


class BodyModel(FastJsonModel):
    recipient: str
    subject: str
    body: str
    immediately: Optional[bool] = settings.NOTIFICATION_IMMEDIATELY
    log_it: Optional[bool] = settings.NOTIFICATION_LOG_IT
    ttl: Optional[int] = settings.NOTIFICATION_TTL
