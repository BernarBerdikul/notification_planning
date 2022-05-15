from typing import Iterator

import requests
from config.settings import AUTH_SERVICE_PATH_USERS, AUTH_SERVICE_URL
from notification.schemas import UserModel
from notification.services import (
    AbstractMessageGenerator,
    FakerService,
    render_template,
)

__all__ = ('MailGenerator',)


class MailGenerator(AbstractMessageGenerator):

    def weekly_top_movies(self, email_template) -> Iterator[tuple[str, str, str]]:
        """
                В зависимости от письма, возвращает в виде генератора данные:
                - электронную почту пользователя;
                - заголовок письма;
                - тело письма.
                """
        my_faker: FakerService = FakerService()
        movies = my_faker.get_popular_movies()

        users_response = requests.post(
            url=f'{AUTH_SERVICE_URL}{AUTH_SERVICE_PATH_USERS}',
            json={
                'jsonrpc': '2.0',
                'method': 'Users.index',
                'params': {
                    'page': 1,
                    'page_size': 10,
                },
                'id': '1',
            },
        )
        users: list[UserModel] = [
            UserModel(**user)
            for user in users_response.json()['result']['users']
        ]
        for user in users:
            rendered_subject: str = render_template(
                html_template=email_template.subject,
                context={'user': user},
            )
            rendered_body: str = render_template(
                html_template=email_template.email_text,
                context={'user': user, 'movies': movies},
            )
            yield user.email, rendered_subject, rendered_body

    def personal_film_selection(self) -> Iterator[tuple[str, str, str]]:
        ...

    def latest_new_movies(self) -> Iterator[tuple[str, str, str]]:
        ...

    def movie_watch_statistic(self) -> Iterator[tuple[str, str, str]]:
        ...
