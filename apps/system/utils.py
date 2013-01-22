 # -*- coding: utf-8 -*-

from datetime import date, datetime
import urllib2, urllib
import hashlib
import random
import string
import time

def get_client_ip(request):
    try:
        real_ip = request.META['HTTP_X_FORWARDED_FOR']
        regip = real_ip.split(",")[0]
    except:
        try:
            regip = request.META['REMOTE_ADDR']
        except:
            regip = ""
    return regip

def get_salt(n=6):
    samples = string.letters + string.digits
    salt = "".join(random.sample(samples, n))
    return salt

def readable_time(t=time.time(), format='%Y-%m-%d %H:%M:%S'):
    gmt = time.localtime(t)
    res = time.strftime(format, gmt)
    return res