from notification.schemas import FastJsonModel

__all__ = ('UserModel',)


class UserModel(FastJsonModel):
    username: str
    email: str
