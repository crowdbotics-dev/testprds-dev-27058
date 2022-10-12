from django.conf import settings
from django.db import models


class NewModel(models.Model):
    "Generated Model"
    cost = models.BigIntegerField()


class Testedhimanshu(models.Model):
    "Generated Model"
    test = models.BigIntegerField()
