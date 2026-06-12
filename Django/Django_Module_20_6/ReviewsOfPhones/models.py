from django.db import models


class Review (models.Model):
    nik_name = models.CharField(blank=False, max_length=30)
    email = models.EmailField(blank=False)
    stars = models.IntegerField(blank=False)
    description = models.CharField(max_length= 250)
