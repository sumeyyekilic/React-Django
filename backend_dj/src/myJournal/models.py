from django.db import models

# Create your models here.
class bulletJournal(models.Model):
    title=models.CharField(max_length=100)
    contentt=models.TextField()

    def __str__(self):
        return self.title
    