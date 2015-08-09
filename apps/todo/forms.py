#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django import forms

class RegisterForm(forms.Form):
    username=forms.CharField(max_length=50,required=True,error_messages={'required':u'用户名不能为空'})
    password=forms.CharField(widget=forms.PasswordInput,required=True)
    password2=forms.CharField(label='Confirm',widget=forms.PasswordInput,required=True)

    def pwd_validate(self,p1,p2):
        return p1==p2

class LoginForm(forms.Form):
    username=forms.CharField(required=True)
    password=forms.CharField(widget=forms.PasswordInput,required=True)