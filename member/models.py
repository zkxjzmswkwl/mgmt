from django.contrib.auth.models import AbstractUser


class Member(AbstractUser):
    pass

    def __str__(self):
        return self.username
