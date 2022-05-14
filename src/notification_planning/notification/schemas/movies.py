from notification.schemas import FastJsonModel

__all__ = ('MovieModel',)


class MovieModel(FastJsonModel):
    title: str
    description: str
    rating: float
