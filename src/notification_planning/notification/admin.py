from django.contrib import admin
from notification.models import EmailTemplate


@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
    """Админка для модели EmailTemplate."""
    list_display = ("title", "mail_type", "email_text", "subject", "created_at", "updated_at" )

