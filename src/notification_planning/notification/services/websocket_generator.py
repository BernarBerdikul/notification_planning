from typing import Iterator

from notification.services import AbstractMessageGenerator

__all__ = ('WebsocketGenerator',)


class WebsocketGenerator(AbstractMessageGenerator):

    def weekly_top_movies(self, websocket_template) -> Iterator[tuple[str, str, str]]:
        ...

    def personal_film_selection(self) -> Iterator[tuple[str, str, str]]:
        ...

    def latest_new_movies(self) -> Iterator[tuple[str, str, str]]:
        ...

    def movie_watch_statistic(self) -> Iterator[tuple[str, str, str]]:
        ...
