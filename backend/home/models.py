from django.conf import settings
from django.db import models


class Tested(models.Model):
    "Generated Model"
    himanshu = models.BigIntegerField()


class Test(models.Model):
    "Generated Model"
    new = models.BigIntegerField()
