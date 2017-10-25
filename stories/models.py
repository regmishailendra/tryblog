from django.contrib.auth.models import User
from django.db import models


class Story(models.Model):
    title = models.CharField(max_length=50,default='Placeholder Content')
    content = models.CharField(max_length=500,blank=True,null=True,default='Placeholder Content')
    publish = models.DateTimeField(auto_now=False, auto_now_add=True)
    image = models.ImageField(null=True, blank=True,
    #   upload_to="media cdn"
                              )
    user = models.ForeignKey(User,default=4)

    def __str__(self):
        return self.title
