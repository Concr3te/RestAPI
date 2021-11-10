from django.db import models

# Create your models here.

class Quote(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateField()
    text = models.CharField(max_length=100)
