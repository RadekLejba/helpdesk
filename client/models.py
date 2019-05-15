from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

from consultant.models import Category


STATUS_CHOICES = (
    ('Todo', 'Todo'),
    ('In progres', 'In progres'),
    ('Done', 'Done'),
)


class Ticket(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Todo'
    )
    closed = models.DateField(null=True, blank=True)
    created = models.DateField(default=now)
    thread = models.CharField(max_length=200, default='')
    description = models.TextField(max_length=1000)
    priority = models.IntegerField(default=1)
    test = models.CharField(default='test', max_length=100)

    def __str__(self):
        return self.thread
