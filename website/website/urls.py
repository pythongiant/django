from django.conf.urls import  include, url
from django.contrib import admin
from . import home_view
urlpatterns = [
    url(r'^$',home_view.index,name="homepage"),
    url(r'^admin/', admin.site.urls,name="admin"),
    url(r'^music/', include('music.urls')),
]
