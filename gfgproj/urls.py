from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    url(r'^post/comments/', include('fluent_comments.urls')),
    url(r'^ratings/', include('ratings.urls')),
]
