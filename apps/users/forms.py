# -*- coding: utf-8 -*-
from datetime import date
import re

from django import forms
from django.contrib.auth.models import User
from apps.users.models import *


class RegForm(forms.Form):
    username = forms.EmailField(label="Email",
                widget=forms.TextInput(attrs={'class':'txt','value':'请输入注册邮箱','title':'请输入注册邮箱','style':" width:250px;"}))
    password1 = forms.CharField(label="Password",
                widget=forms.PasswordInput(attrs={'class':'txt','title':'创建密码','style':"color:#000000; width:108px;"}))
    password2 = forms.CharField(label="Password confirmation",
                widget=forms.PasswordInput(attrs={'class':'txt','title':'确认密码','style':"color:#000000; width:108px;"}))
    nickname = forms.CharField(label="Nick name",
                widget=forms.TextInput(attrs={'class':'txt','value':'请输入昵称','title':'请输入昵称','style':" width:250px;"}))
    true_name = forms.CharField(label="True name", required=False)
    identity_card_code = forms.CharField(label="Card code", required=False)
    inviter_email = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("邮箱已被使用")
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError('密码不一致')
        return password2

    def clean_nickname(self):
        nickname = self.cleaned_data["nickname"]
        GM_re = re.compile(r'^GM\d+',re.IGNORECASE)
        if re.match(GM_re, nickname):
            raise forms.ValidationError('非法昵称')
        if len(nickname)>10:
            raise forms.ValidationError('昵称应小于10个字符')
        elif len(UserProfile.objects.filter(nickname__iexact=nickname.lower())) > 0:
            raise forms.ValidationError('昵称已被用')
        else:
            return nickname
        
    def clean_true_name(self):
        true_name = self.cleaned_data["true_name"]
        if len(true_name) < 2 and len(true_name) != 0:
            raise forms.ValidationError('姓名不得小于2个英文字母或中文汉字。')
        else:
            return true_name 
        
    def clean_identity_card_code(self):
        identity_card_code = self.cleaned_data['identity_card_code']
        if len(identity_card_code) == 15:
            bs = '19' + identity_card_code[6:12]
            code_re = re.compile(r'^[1-9](\d{14})$')
            if not re.match(code_re, identity_card_code):
                raise forms.ValidationError('非法的身份证号码。')
            try:
                date(int(bs[0:4]), int(bs[4:6]), int(bs[6:8]))
            except ValueError:
                raise forms.ValidationError('非法身份证号')
#            if len(UserProfile.objects.filter(identity_card_code=identity_card_code)) > 0:
#                raise forms.ValidationError('身份证号码已被用')
            return identity_card_code
        elif len(identity_card_code) == 18:
            bs = identity_card_code[6:14]
            code_re = re.compile(r'^[1-9](\d{16})(\d|X|x)$')
            if not re.match(code_re, identity_card_code):
                raise forms.ValidationError('非法的身份证号码。')
            try:
                date(int(bs[0:4]), int(bs[4:6]), int(bs[6:8]))
            except ValueError:
                raise forms.ValidationError('非法的身份证号码。')
            wi = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
            varify_code = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
            input_code = 0
            for i in range(0, 17):
                input_code += wi[i] * int(identity_card_code[i])
            if str(varify_code[input_code%11]) != identity_card_code[17]:
                raise forms.ValidationError('非法的身份证号码。')
#            if len(UserProfile.objects.filter(identity_card_code=identity_card_code)) > 0:
#                raise forms.ValidationError('身份证号码已被用')
            return identity_card_code
        elif len(identity_card_code) == 0:
            return identity_card_code
        else:
            raise forms.ValidationError('非法的身份证号码。')


        

