from django.contrib import admin

# Register your models here.
from post.models import Post, Comment, Like, DisLike

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(DisLike)
