#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import Http404
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from models import Todo
from forms import RegisterForm,LoginForm

# Create your views here.

def todolist(request):
    todolist=Todo.objects.filter(flag=1)
    finishtodos=Todo.objects.filter(flag=0)
    return render_to_response('simpleTodo.html',{'todolist':todolist,'finishtodos':finishtodos},context_instance=RequestContext(request))

def todofinish(request,id):
    todo=Todo.objects.get(id=id)
    if todo.flag=='1':
        todo.flag='0'
        todo.save()
        return HttpResponseRedirect('/todo/')
    todolist=Todo.objects.filter(flag=1)
    return render_to_response('simpleTodo.html',{'todolist':todolist},context_instance=RequestContext(request))

def todoback(request,id):
    todo=Todo.objects.get(id=id)
    if todo.flag=='0':
        todo.flag='1'
        todo.save()
        return HttpResponseRedirect('/todo/')
    todolist=Todo.objects.filter(flag=1)
    return render_to_response('simpleTodo.html',{'todolist':todolist},context_instance=RequestContext(request))

def tododelete(request,id):
    try:
        todo=Todo.objects.get(id=id)
    except Exception:
        raise Http404
    if todo:
        todo.delete()
        return HttpResponseRedirect('/todo/')
    todolist=Todo.objects.filter(flag=1)
    return render_to_response('simpleTodo.html',{'todolist':todolist},context_instance=RequestContext(request))

def addtodo(request):
    if request.method=='POST':
        atodo=request.POST['todo']
        priority=request.POST['priority']
        user=User.objects.get(id='1')
        todo=Todo(user=user,todo=atodo,priority=priority,flag='1')
        todo.save()
        todolist = Todo.objects.filter(flag='1')
        finishtodos = Todo.objects.filter(flag=0)
        return render_to_response('showtodo.html',{'todolist':todolist,'finishtodos':finishtodos},context_instance=RequestContext(request))
    else:
        todolist = Todo.objects.filter(flag=1)
        finishtodos = Todo.objects.filter(flag=0)
        return render_to_response('simpleTodo.html',{'todolist':todolist,'finishtodos':finishtodos},context_instance=RequestContext(request))

def updatetodo(request,id):
    if request.method=='POST':
        try:
            todo=Todo.objects.get(id=id)
        except Exception:
            return HttpResponseRedirect('/todo/')
        atodo=request.POST['todo']
        priority = request.POST['priority']
        # user = User.objects.get(id='1')
        todo.todo=atodo
        todo.priority=priority
        todo.save()
        return HttpResponseRedirect('/todo/')
    else:
        try:
            todo = Todo.objects.get(id=id)
        except Exception:
            raise Http404
        return render_to_response('updatetodo.html',{'todo':todo},context_instance=RequestContext(request))

def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            # print request.user
            return HttpResponseRedirect('/todo/')
        else:
            return HttpResponseRedirect('/todo/base/')
    else:
        return render_to_response('login.html',context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    # return base(request)
    return HttpResponseRedirect('/todo/base/')

def base(request):
    return render_to_response('base-todo.html')

def register(request):
    error=[]
    if request.method=='POST':
        form=RegisterForm(request.POST)
        print form
        if form:
            data=form.cleaned_data
            username=data['username']
            password=data['password']
            password2=data['password2']
            print username
            print password
            print password2
            if not User.objects.filter(username=username):
                if form.pwd_validate(password,password2):
                    user=User.objects.create_user(username=username,password=password)
                    user.save()
                    login_view(request)
                    return HttpResponseRedirect('/todo/')
                else:
                    error.append('两次输入的密码不一致!')
            else:
                error.append('用户已存在!')
    else:
        return render_to_response('register.html',locals(),context_instance=RequestContext(request))

# def register(request):
#     def pwd_validate(p1,p2):
#         return p1==p2
#     error=[]
#     if request.method=='POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         password2=request.POST['password2']
#         if not User.objects.filter(username=username):
#             if pwd_validate(password,password2):
#                 user=User.objects.create_user(username=username,password=password)
#                 user.save()
#                 login_view(request)
#                 return HttpResponseRedirect('/todo/')
#             else:
#                 error.append('两次输入的密码不一致!')
#                 # return HttpResponse('<p>两次的密码不一致</p>')
#                 return render_to_response('register.html',locals(),context_instance=RequestContext(request))
#         else:
#             error.append('用户已存在!')
#             return render_to_response('register.html',locals(),context_instance=RequestContext(request))
#     else:
#         return render_to_response('register.html',locals(),context_instance=RequestContext(request))

def page404(request):
    return render_to_response('404.html')