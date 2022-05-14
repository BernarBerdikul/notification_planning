from abc import ABC, abstractmethod
from typing import Iterator, Optional

__all__ = ('AbstractMailGenerator', 'mail_generator', 'get_mail_generator')


class AbstractMailGenerator(ABC):

    @abstractmethod
    def weekly_top_movies(self, email_template) -> Iterator[tuple[str, str, str]]:
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


mail_generator: Optional[AbstractMailGenerator] = None


def get_mail_generator() -> AbstractMailGenerator:
    return mail_generator
