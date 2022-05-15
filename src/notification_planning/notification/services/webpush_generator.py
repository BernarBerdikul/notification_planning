from typing import Iterator

from notification.services import AbstractMessageGenerator

__all__ = ('WebpushGenerator',)


class WebpushGenerator(AbstractMessageGenerator):

    def weekly_top_movies(self, webpush_template) -> Iterator[tuple[str, str, str]]:
        ...

    def personal_film_selection(self) -> Iterator[tuple[str, str, str]]:
        ...

    def latest_new_movies(self) -> Iterator[tuple[str, str, str]]:
        ...

    def movie_watch_statistic(self) -> Iterator[tuple[str, str, str]]:
        ...
