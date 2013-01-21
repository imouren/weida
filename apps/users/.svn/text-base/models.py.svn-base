# -*- coding: utf-8 -*-

from django.db import models
from django.core.cache import cache
from datetime import date, datetime, timedelta

GENDERS = (
    ('F', '女'),
    ('M', '男'),
)

CACHE_USER = 'user_%s' #%s is uid

class UserProfile(models.Model):
    uid = models.IntegerField(primary_key=True) # foreignkey User Model
    nickname = models.CharField(max_length=50,unique=True)
    avatar = models.CharField(max_length=100, default='')
    true_name = models.CharField(default = '', max_length=50)
    identity_card_code = models.CharField(max_length=32)
    gender = models.CharField(default = 'F', max_length=1, choices=GENDERS, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    city = models.CharField(default = '', max_length=20, blank=True, null=True)
    address = models.CharField(default = '', max_length=200, blank=True, null=True)
    msn = models.CharField(default = '', max_length=50, blank=True, null=True)
    qq = models.CharField(default = '', max_length=20, blank=True, null=True)
    gtalk = models.CharField(default = '', max_length=50, blank=True, null=True)
    description = models.CharField(default = '', max_length=255, blank=True, null=True)
    only_friends = models.BooleanField(default=False)
    mobile = models.CharField(default = '', max_length=20, blank=True, null=True)
    come_from = models.CharField(default = '', max_length=20, blank=True, null=True)
    is_mobile_bundle = models.BooleanField(default=False)
    disabled_time = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return '%s' % self.uid

    def save(self,force_insert=False,force_update=False):
        super(UserProfile,self).save()
        self.update_cache()

    def update_cache(self):
        key = CACHE_USER % self.uid
        cache.set(key,self)

