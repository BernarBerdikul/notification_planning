from django.contrib import admin
from notification.models import EmailTemplate


@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
    """Админка для модели EmailTemplate."""
    list_display = (
        'id', 'title', 'mail_type',
        'is_send_immediately', 'is_log_it',
        'created_at', 'updated_at',
    )
    list_display_links = (
        'id', 'title',
    )
    list_filter = (
        'mail_type',
        'is_send_immediately',
        'is_log_it',
    )
    fields = (
        'title', 'mail_type',
        'subject', 'email_text',
        'is_send_immediately', 'is_log_it',
    )
    search_fields = (
        'id',
        'title',
    )
