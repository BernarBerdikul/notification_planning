from django.apps import AppConfig


class NotificationConfig(AppConfig):
    """Настройки приложения."""

    name = 'notification'

    # def ready(self):
    #     from notification.services import *
    #     # Mail Generator
    #     mail_generator = DummyMailGenerator()
