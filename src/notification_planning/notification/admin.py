from django.contrib import admin
from notification.models import MessageTemplate


@admin.register(MessageTemplate)
class MessageTemplateAdmin(admin.ModelAdmin):
    """Админка для модели MessageTemplate."""
    list_display = (
        'id', 'title', 'mail_type', 'channel',
        'is_send_immediately', 'is_log_it',
        'created_at', 'updated_at',
    )
    list_display_links = (
        'id', 'title',
    )
    list_filter = (
        'mail_type',
        'channel',
        'is_send_immediately',
        'is_log_it',
    )
    fields = (
        'title', 'mail_type', 'channel',
        'subject', 'email_text',
        'is_send_immediately', 'is_log_it',
    )
    search_fields = (
        'id',
        'title',
    )
