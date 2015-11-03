"""familiesdb URL Configuration

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
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    #Info urls
    url(r'^$', 'families.views.home.home', name='home'),

    #Relatives urls
    url(r'^relatives/$', 'families.views.relatives.relatives_list', name='relative_list'),
    url(r'^relatives/add/$', 'families.views.relatives.relatives_add', name='relatives_add'),
    url(r'^relatives/(?P<rid>\d+)/edit/$', 'families.views.relatives.relatives_edit', name='relatives_edit'),
    url(r'^relatives/(?P<rid>\d+)/native/$', 'families.views.relatives.relatives_native', name='relatives_native'),
    url(r'^relatives/(?P<rid>\d+)/info/$', 'families.views.relatives.relatives_info', name='relatives_info'),
    url(r'^relatives/(?P<rid>\d+)/delete/$', 'families.views.relatives.relatives_delete', name='relatives_delete'),

    #Generations urls
    url(r'^generations/$', 'families.views.generations.generations_list', name='generations'),

    #Tree's urls
    url(r'^tree/', 'families.views.tree.tree', name='tree'),

    url(r'^admin/', include(admin.site.urls)),
)

from .settings import MEDIA_ROOT, DEBUG

if DEBUG:
    # serve files from media folder
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': MEDIA_ROOT}))