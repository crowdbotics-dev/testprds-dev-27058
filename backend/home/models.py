from django.conf import settings
from django.db import models


class Tested(models.Model):
    "Generated Model"
    himanshu = models.BigIntegerField()
    yes = models.URLField(
        null=True,
        blank=True,
    )
