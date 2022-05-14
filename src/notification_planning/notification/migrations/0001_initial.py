# Generated by Django 3.2.9 on 2022-05-14 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Наименование')),
                ('mail_type', models.CharField(choices=[('welcome_letter', 'Приветственное письмо'), ('selection_movies', 'Подборка фильмов'), ('personal_newsletter', 'Персональная рассылка фильмов'), ('user_statistic', 'Статистика просмотров пользователя')], max_length=50, unique=True, verbose_name='Тип сообщения')),
                ('subject', models.TextField(blank=True, null=True, verbose_name='Тема сообщения')),
                ('email_text', models.TextField(verbose_name='Шаблон сообщения')),
                ('is_send_immediately', models.BooleanField(default=False, verbose_name='Отправить мгновенно')),
                ('is_log_it', models.BooleanField(default=False, verbose_name='Логировать')),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'email_templates',
            },
        ),
    ]
