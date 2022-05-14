import abc

class AbstractMailGenerator:
    @abc.abstractmethod
    def personal_film_selection(self) -> None:
        # """Сохранить состояние в постоянное хранилище"""
        pass

    @abc.abstractmethod
    def latest_new_movies(self) -> dict:
        # """Загрузить состояние локально из постоянного хранилища"""
        pass

    @abc.abstractmethod
    def movie_watch_statistic(self) -> dict:
        # """Загрузить состояние локально из постоянного хранилища"""
        pass


# from os import path, environ
# from sys import path as sys_path
# from django import setup
#
# sys_path.append("/config/settings.py")
# environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
# setup()

from notification.models import EmailTemplate

template = EmailTemplate.objects.filter(mail_type="welcome_letter").first()
a = 9
from collections import namedtuple

a = 7

from jinja2 import Template
from typing import Iterator, Tuple


def get_users():
    User = namedtuple('User', 'email name lastname')
    users = []
    for i in range(10):
        email = f"email{i}@mailtest.ru"
        name = f"Tony_the_{i}"
        last = f"Stark_the_{i}"
        users.append(User(email, name, last))
    return users

def get_films():
    Film = namedtuple('Film', 'title url')
    films = []
    for i in range(10):
        title = f"Iron man episode {i + 1}"
        url = f"Kinoteatr.ru/movies/iron_man/{i}"
        films.append(Film(title, url))
    return films




class DummyMailGenerator(AbstractMailGenerator):
    def __init__(self, template: EmailTemplate):
        self.context = template.mail_type
        self.text = template.email_text

    def personal_film_selection(self) -> Iterator[Tuple[str, str]]:
        users = get_users()
        films = get_films()
        template = Template(self.text)
        for user in users:
            recipient = user.email
            html = template.render(user=user, films=films)
            yield recipient, html


    def latest_new_movies(self) -> dict:
        # """Загрузить состояние локально из постоянного хранилища"""
        users = get_users()
        films = get_films()
        template = Template(self.text)
        for user in users:
            recipient = user.email
            html = template.render(user=user, films=films)
            yield recipient, html


    # def movie_watch_statistic(self) -> dict:
    #     # """Загрузить состояние локально из постоянного хранилища"""
    #     users = get_users()
    #     films = get_films()
    #     template = Template(self.text)
    #     for user in users:
    #         recipient = user.email
    #         html = template.render(user=user, films=films)
    #         yield recipient, html



