from django.contrib import admin
from forum.models import Post, PostReply


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']


class PostReplyAdmin(admin.ModelAdmin):
    list_display = ['content', 'author', 'post']


admin.site.register(Post, PostAdmin)
admin.site.register(PostReply)




