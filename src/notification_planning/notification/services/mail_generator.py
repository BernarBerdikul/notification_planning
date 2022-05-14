from typing import Iterator

from notification.services.abstract_mail_generator import AbstractMailGenerator

__all__ = ('MailGenerator',)


class MailGenerator(AbstractMailGenerator):

    def weekly_top_movies(self, email_template) -> Iterator[tuple[str, str, str]]:
        ...

    def personal_film_selection(self) -> Iterator[tuple[str, str, str]]:
        ...

    def latest_new_movies(self) -> Iterator[tuple[str, str, str]]:
        ...

    def movie_watch_statistic(self) -> Iterator[tuple[str, str, str]]:
        ...
