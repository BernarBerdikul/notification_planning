from notification.schemas import FastJsonModel

__all__ = ('UserModel',)


class UserModel(FastJsonModel):
    first_name: str
    last_name: str
    email: str
