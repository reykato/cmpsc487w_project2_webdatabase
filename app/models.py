from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image_url = models.CharField(max_length=200)

    class Meta:
        ordering = ["name", "id"]

    def __str__(self):
        return f"{self.id} {self.name} {self.description}"