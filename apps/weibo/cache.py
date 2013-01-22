# -*- coding: utf-8 -*-

import cPickle
import sys
from django.core.cache import cache
from apps.weibo.models import *

def get_or_create_user_weibo(uid):
    key = CACHE_KEY_USER_WEIBO = 'cache_user_weibo_%s'
    res = cache.get(key)
    if not res:
        try:
            res = UserWeibo.objects.get(uid=uid)
        except:
            res = UserWeibo(uid=uid)
            res.save()
        cache.set(key, res)
    return res

def update_user_weibo(uid, access_token, expires_in):
    u_weibo = get_or_create_user_weibo(uid)
    u_weibo.access_token = access_token
    u_weibo.expires_in = expires_in
    u_weibo.save()
    return u_weibo
