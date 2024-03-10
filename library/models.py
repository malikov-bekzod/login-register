from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 60)
    description = models.TextField()
    price = models.FloatField()
    count = models.PositiveIntegerField(default = 1)
    last_update = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title