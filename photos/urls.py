from django.conf.urls import patterns, url

urlpatterns = patterns('.views',
    url(r'^list/$', 'list', name='list'),
)