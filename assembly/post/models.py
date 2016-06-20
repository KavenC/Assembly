from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Group(models.Model):
    author = models.ForeignKey(User, related_name='groups_created')
    teammates = models.ManyToManyField(User, related_name='groups_joined')
    title = models.CharField(max_length=200)
    game = models.CharField(max_length=100)
    stage = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "[%s][%s] %s" % (self.game, self.stage, self.title)
