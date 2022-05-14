import requests
from faker import Faker
from notification.schemas import MovieModel, UserModel

__all__ = ('FakerService',)


class FakerService:

    def __init__(self):
        self.fake = Faker()
        self.count = 10

    def get_users(self) -> list[UserModel]:
        """Возвращает сгенерированных фейковых пользователей."""
        return [
            UserModel(
                first_name=self.fake.first_name(),
                last_name=self.fake.last_name(),
                email=self.fake.email(),
            )
            for _ in range(self.count)
        ]

    def get_popular_movies(self) -> list[MovieModel]:
        """Возвращает популярные фильмы."""

        # Запрашиваем {self.count} популярных фильмов с `https://yts.mx`
        response = requests.get(
            url=f'https://yts.mx/api/v2/list_movies.json?sort_by=rating&limit={self.count}',
        )
        movies_title: list[str] = [
            movie['title']
            for movie in response.json()['data']['movies']
        ]
        return [
            MovieModel(
                title=title,
                description=self.fake.text(),
                rating=self.fake.random.randint(0, 10),
            )
            for title in movies_title
        ]
