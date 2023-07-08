from django.db import models
from django.contrib.auth.models import User

class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    input1 = models.FloatField()
    input2 = models.FloatField()
    input3 = models.FloatField()
    input4 = models.FloatField()
    input5 = models.FloatField()
    input6 = models.FloatField()
    input7 = models.FloatField()
    input8 = models.FloatField()
    input9 = models.FloatField()
    output = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)