from django.conf.urls import patterns, include, url
from django.contrib import admin
from blogDemo.blog import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', views.index),
    url(r'^home/(?P<slug>[\w\-]+)/$','blogDemo.blog.views.post'),
)
