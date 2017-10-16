from django.contrib.auth.models import User
from django.db import models


class Story(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    publish = models.DateTimeField(auto_now=False, auto_now_add=True)
    image = models.FileField(null=True, blank=True)
    user = models.ForeignKey(User,default=4)

    def __str__(self):
        return self.title
