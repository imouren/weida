# -*- coding: utf-8 -*-

from django.db import models
from django.core.cache import cache
from datetime import date, datetime, timedelta
import time


CACHE_KEY_USER_WEIBO = 'cache_user_weibo_%s' #%s is uid

class UserWeibo(models.Model):
    uid = models.IntegerField(primary_key=True) # foreignkey User Model
    access_token = models.CharField(max_length=50, default='')
    expires_in = models.IntegerField(default=int(time.time()))

    def update_cache(self):
        key = CACHE_KEY_USER_WEIBO % (self.uid)
        cache.set(key, self)
    
    def delete_cache(self):
        key = CACHE_KEY_USER_WEIBO % (self.uid)
        cache.delete(key)
    
    def save(self):
        super(UserWeibo, self).save()
        self.update_cache()
    
    def delete(self):
        self.delete_cache()
        super(UserWeibo, self).delete()

    def __unicode__(self):
        return '%s' % self.uid

    class Meta:
        db_table = 'wd_userweibo'

