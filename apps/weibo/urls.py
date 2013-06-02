# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('apps.weibo.views',
    (r'^$', 'index'),
    (r'^callback/$', 'callback'),
    (r'^authorize/$', 'authorize_weibo'),
    (r'^send_weibo/$', 'send_weibo'),
    (r'^twitter_my_wife/$', 'twitter_my_wife'),
)
        

