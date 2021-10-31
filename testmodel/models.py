from django.db import models

# Create your models here.
from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=256)


class Changes(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=10)
