from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    jobChoice = (('D', 'Desenvolvedor'), ('G', 'Gerente'), ('V', 'Vendedor'),)
    job = models.CharField(max_length=1, choices=jobChoice)

