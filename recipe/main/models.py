from django.db import models
from django.contrib.auth.models import AbstractUser

class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Пpoшeл активацию?')
    send_messages = models.BooleanField(default=False, verbose_name='Слать оповещения о новых рецептах?')
    class Meta(AbstractUser.Meta):
        pass