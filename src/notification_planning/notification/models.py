from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils import timezone


class TemplateCodes(models.TextChoices):
    """Коды шаблонов."""

    welcome_letter = "welcome_letter", "Приветственное письмо"
    selection_movies = "selection_movies", "Подборка фильмов"
    personal_newsletter = "personal_newsletter", "Персональная рассылка фильмов"
    user_statistic = "user_statistic", "Статистика просмотров пользователя"


class EmailTemplate(models.Model):
    """Модель для хранения шаблона письма."""

    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name="Наименование", max_length=250)
    mail_type = models.CharField(verbose_name="Тип сообщения", choices=TemplateCodes.choices, max_length=50)
    email_text = models.TextField(verbose_name="Шаблон сообщения")
    subject = models.TextField(verbose_name="Тема сообщения", blank=True, null=True)

    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        """Сохраннение экземпляра."""
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.mail_type)

    class Meta:
        db_table = 'email_templates'

