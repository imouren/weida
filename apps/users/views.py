# -*- coding: utf-8 -*-

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext, Context
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.utils import simplejson
from apps.users.helper import *
from apps.users.cache import *
from apps.users.forms import *

def index(request):
    data = {}
    return render_to_response('users/index.html',data,context_instance=RequestContext(request))

@login_required
def home(request):
    return HttpResponse('home')

def user_logout(request):
    if request.user.is_authenticated():
        logout(request)

    hr = HttpResponseRedirect('/')
    return hr

def user_login(request):
    data = {'media_url':settings.MEDIA_URL}
    if request.method == 'GET':
        reg_form = RegForm(initial={'inviter_email':request.GET.get('i')})
        data['reg_form'] = reg_form
        redirect_url = request.GET.get('next')
        if not redirect_url:redirect_url='/'
        data['next'] = redirect_url
        return render_to_response('users/login.html',data,context_instance=RequestContext(request))
    else:
        form = AuthenticationForm(data=request.POST)
        redirect_url = request.POST.get('next', '/')
        username = request.POST.get('username', '')
        password_str = request.POST.get('password', '')
        if form.is_valid():
            username = form.cleaned_data.get("username", "")
            password_str = form.cleaned_data.get("password", "")
            user = authenticate(username=username, password=password_str)
            regip = get_client_ip(request)
            
            login(request, user)
            request.session.set_expiry(3600*12)
            resp = HttpResponseRedirect(redirect_url)
            return resp
        else:
            reg_form = RegForm(initial={'inviter_email':request.GET.get('i')})
            data['reg_form'] = reg_form
            err_info = u"用户名密码错误"
            data['err_info'] = err_info
            data['next'] = redirect_url
            return render_to_response('users/login.html',data,
                                  context_instance=RequestContext(request))

def register(request):
    data = {'media_url':settings.MEDIA_URL}
    if request.session.has_key('come_from'):
        come_from = request.session['come_from']
    else:
        come_from = ''

    if request.method == "GET":
        return render_to_response('users/register.html', data,
                                  context_instance=RequestContext(request))
    form = RegForm(request.POST)

    redirect_url = request.POST.get('next', '/')
    if form.is_valid():
        user = User(username=form.cleaned_data['username'], is_active=True)
        user.set_password(form.cleaned_data['password1'])
        user.save()

        profile = UserProfile(uid=user.id, nickname=form.cleaned_data['nickname'],
                              true_name=form.cleaned_data['true_name'],
                              come_from = come_from,
                              identity_card_code=form.cleaned_data['identity_card_code'])
        profile.save()
        
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        login(request, user)

        request.session.set_expiry(3600*12)
        resp = HttpResponseRedirect(redirect_url)
        return resp
    else:
        data['reg_form'] = form
        data['errors'] = dict(form.errors.items())
        data['next'] = redirect_url
        return render_to_response('users/register.html', data,
                                  context_instance=RequestContext(request))


