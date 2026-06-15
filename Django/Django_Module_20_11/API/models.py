from django.db import models

class Prediction(models.Model):
    content = models.CharField(100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(null=True)

class Moment(models.Model):
    content = models.CharField(100)
    created_at = models.DateTimeField()
    update_at = models.DateTimeField(null=True)

class FullPrediction(models.Model):
    moment = models.CharField(100)
    prediction = models.CharField(100)
