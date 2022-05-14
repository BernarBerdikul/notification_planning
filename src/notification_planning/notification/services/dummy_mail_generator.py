from typing import Iterator

from notification.services import AbstractMailGenerator, FakerService, render_template

__all__ = ('DummyMailGenerator',)


class DummyMailGenerator(AbstractMailGenerator):

    def weekly_top_movies(self, email_template) -> Iterator[tuple[str, str, str]]:
        """
        В зависимости от письма, возвращает в виде генератора данные:
        - инфо о пользователе;
        - заголовок письма;
        - тело письма.
        """
        my_faker: FakerService = FakerService()
        users = my_faker.get_users()
        movies = my_faker.get_popular_movies()
        for user in users:
            rendered_subject: str = render_template(
                html_template=email_template.subject,
                context={
                    'user': user,
                    'movies': movies,
                },
            )
            rendered_body: str = render_template(
                html_template=email_template.email_text,
                context={'movies': movies},
            )
            yield user, rendered_subject, rendered_body

    def personal_film_selection(self) -> Iterator[tuple[str, str, str]]:
        return []

    def latest_new_movies(self) -> Iterator[tuple[str, str, str]]:
        return []

    def movie_watch_statistic(self) -> Iterator[tuple[str, str, str]]:
        return []
