from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField(max_length=200)
    instructions = models.TextField()

    def __str__(self):
        return self.name