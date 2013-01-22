# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('apps.users.views',
    (r'^$', 'user_login'),
    (r'^logout/$', 'user_logout'),
    (r'^login/$', 'user_login'),
    (r'^register/$', 'register'),
)
        

