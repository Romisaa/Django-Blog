from django.contrib import admin
from .models import Post


# to register our posts in admin site
admin.site.register(Post)
