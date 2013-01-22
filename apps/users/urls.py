# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('apps.users.views',
    (r'^$', 'ulogin'),
    (r'^logout/$', 'user_logout'),
    (r'^login/$', 'ulogin'),
    (r'^register/$', 'register'),
)
        

