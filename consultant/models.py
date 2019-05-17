from django.db import models


class Category(models.Model):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
