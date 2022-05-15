from typing import Iterator

from notification.services.abstract_message_generator import AbstractMessageGenerator

__all__ = ('MailGenerator',)


class MailGenerator(AbstractMessageGenerator):

    def weekly_top_movies(self, email_template) -> Iterator[tuple[str, str, str]]:
        ...

    def personal_film_selection(self) -> Iterator[tuple[str, str, str]]:
        ...

    def latest_new_movies(self) -> Iterator[tuple[str, str, str]]:
        ...

    def movie_watch_statistic(self) -> Iterator[tuple[str, str, str]]:
        ...
