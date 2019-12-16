from django.db import models

# Create your models here.
class Test(models.Model):
    title = models.TextField()
    floors = models.IntegerField(null=True, blank=True)
    windows = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title