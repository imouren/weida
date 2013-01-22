# -*- coding: utf-8 -*-

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext, Context
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import simplejson
from apps.weibo.cache import *
from thirdparty.weibo_api import *
from apps.system.utils import *

@login_required
def index(request):
    uid = request.user.id
    u_weibo = get_or_create_user_weibo(uid)
    now = int(time.time())
    end_time = u_weibo.expires_in
    if end_time > now:
        need_authorize = False
    else:
        need_authorize = True
    data = {'need_authorize':need_authorize, 'end_time':readable_time(end_time)}
    return render_to_response('weibo/index.html',data,context_instance=RequestContext(request))

@login_required
def authorize_weibo(request):
    client = get_weibo_client()
    url = client.get_authorize_url()
    return HttpResponseRedirect(url)

@login_required
def callback(request):
    code = request.GET.get('code')
    uid = request.user.id
    client = get_weibo_client()
    r = client.request_access_token(code)
    u_weibo = update_user_weibo(uid, r.access_token, r.expires_in)
    return HttpResponseRedirect('/weibo/')

@login_required
def send_weibo(request):
    uid = request.user.id
    u_weibo = get_or_create_user_weibo(uid)
    client = get_weibo_client()
    client.set_access_token(u_weibo.access_token, u_weibo.expires_in)
    info = 'test'+ time.time()
    client.statuses.update.post(status=info)
    return HttpResponse('ok')
