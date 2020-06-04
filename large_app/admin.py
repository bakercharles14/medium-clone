from django.contrib import admin
from .models import Post, User, Comment, Clap

admin.site.register([Post, User, Comment, Clap])

# can also register models individually
# admin.site.register(Post)
# admin.site.register(User)
# admin.site.register(Comment)
# admin.site.register(Clap)
