from django.contrib import admin
from .models import Post
from django_comments.models import CommentFlag, BaseCommentAbstractModel, CommentAbstractModel, Comment

admin.site.register(Post)

admin.site.register(CommentFlag)
