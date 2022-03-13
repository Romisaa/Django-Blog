from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Creating a class post that will save our post data into database by inheriting some models from django
class Post(models.Model):
    title = models.CharField(max_length=100)
    Content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    
    #This is a function to make the returing value from Post.objects.all more descriptive as it will return the post's title.
    def __str__(self):
        return self.title

    # create a reverse function to tell django how to find url
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


