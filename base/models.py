from django.db import models

# Create your models here.

class UrlTable(models.Model):

    name = models.CharField(max_length=1000, null=True)
    uuid = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name
