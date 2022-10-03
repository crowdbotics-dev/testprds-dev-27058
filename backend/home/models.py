from django.conf import settings
from django.db import models


class Tested(models.Model):
    "Generated Model"
    himanshu = models.BigIntegerField()


class NewModel(models.Model):
    "Generated Model"
    cost = models.BigIntegerField()
