from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'hello.views.blankForm'),
    url(r'^andrew', 'hello.views.andrew'),
)
