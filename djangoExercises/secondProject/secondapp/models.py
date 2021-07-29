from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    blogTitle = models.CharField(max_length = 100)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    createdOn = models.DateTimeField(auto_now = True)
    content = models.TextField()

    def __str__(self):
        return self.blogTitle