from django.db import models

# Create your models here.
class Shout(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.title + ': ' + self.content