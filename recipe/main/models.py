from django.db import models
from django.contrib.auth.models import AbstractUser

class AdvUser(AbstractUser):
    send_messages = models.BooleanField(default=False, verbose_name='Слать оповещения о новых рецептах?')
    class Meta(AbstractUser.Meta):
        pass