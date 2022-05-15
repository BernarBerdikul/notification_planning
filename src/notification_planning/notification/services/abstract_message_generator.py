from abc import ABC, abstractmethod
from typing import Iterator, Optional

__all__ = ('AbstractMessageGenerator', 'message_generator', 'get_message_generator')


class AbstractMessageGenerator(ABC):

    @abstractmethod
    def weekly_top_movies(self, message_template) -> Iterator[tuple[str, str, str]]:
        pass

    @abstractmethod
    def personal_film_selection(self) -> Iterator[tuple[str, str, str]]:
        pass

    @abstractmethod
    def latest_new_movies(self) -> Iterator[tuple[str, str, str]]:
        pass

    @abstractmethod
    def movie_watch_statistic(self) -> Iterator[tuple[str, str, str]]:
        pass


message_generator: Optional[AbstractMessageGenerator] = None


def get_message_generator() -> AbstractMessageGenerator:
    return message_generator
