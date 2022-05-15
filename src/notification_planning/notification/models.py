from django.db import models
from django.utils import timezone


class TemplateCodes(models.TextChoices):
    """Коды шаблонов."""

    welcome_letter = 'welcome_letter', 'Приветственное письмо'
    selection_movies = 'selection_movies', 'Подборка фильмов'
    personal_newsletter = 'personal_newsletter', 'Персональная рассылка фильмов'
    user_statistic = 'user_statistic', 'Статистика просмотров пользователя'


class NotifyChannel(models.TextChoices):
    """Каналы уведомлений."""

    email = 'email', 'Почта'
    websocket = 'websocket', 'Websocket'
    web_push = 'web_push', 'Push уведомление'


class MessageTemplate(models.Model):
    """Модель для хранения шаблона сообщения."""

    title = models.CharField(
        verbose_name='Наименование', max_length=250,
    )
    mail_type = models.CharField(
        verbose_name='Тип сообщения',
        choices=TemplateCodes.choices,
        max_length=50, unique=True,
    )
    channel = models.CharField(
        verbose_name='Канал уведомления',
        choices=NotifyChannel.choices,
        max_length=50, unique=True,
    )
    subject = models.TextField(
        verbose_name='Тема сообщения', blank=True, null=True,
    )
    email_text = models.TextField(
        verbose_name='Шаблон сообщения',
    )
    is_send_immediately = models.BooleanField(
        verbose_name='Отправить мгновенно', default=False,
    )
    is_log_it = models.BooleanField(
        verbose_name='Логировать', default=False,
    )

    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs) -> 'MessageTemplate':
        """Сохраннение экземпляра."""
        if not self.pk:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.pk}: {self.mail_type} - {self.subject}'

    class Meta:
        db_table = 'message_templates'
