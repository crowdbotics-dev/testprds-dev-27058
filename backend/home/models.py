from django.conf import settings
from django.db import models


class NewModel(models.Model):
    "Generated Model"
    cost = models.BigIntegerField()
