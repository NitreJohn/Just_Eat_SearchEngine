"""hw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'hw.hw.index'),
    url(r'^hw/$', 'hw.hw.indexhw'),
    url(r'^time/$', 'hw.time.current_datetime'),
    url(r'^time/plus/()\d{1,2}/', 'hw.time.hours_ahead'),
    url(r'^static/(?P<path>.*)$',  'django.views.static.serve', {'document_root': settings.STATICFILES_DIRS[0]}),
    url(r'^wiki/(?P<path>.*)$',  'django.views.static.serve', {'document_root': settings.STATICFILES_DIRS[1]}),
    url(r'^food/search/static/(?P<path>.*)$',  'django.views.static.serve', {'document_root': settings.STATICFILES_DIRS[2]}),
    url(r'^food/search/$', 'hw.search.findID'),
    url(r'^template/$', 'hw.template.index'),
]
