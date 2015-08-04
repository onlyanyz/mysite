from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import Http404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from models import Todo

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
    user=authenticate(username=request.POST['username'],password=request.POST['password'])
    if user is not None:
        login(request,user)
        print request.user
        return HttpResponseRedirect('/todo/')
    else:
        return HttpResponseRedirect('/todo/base/')

def logout_view(request):
    logout(request)
    # return base(request)
    return HttpResponseRedirect('/todo/base/')

def base(request):
    return render_to_response('base-todo.html')

def login_page(request):
    return render_to_response('login.html',context_instance=RequestContext(request))

def register(request):
    return render_to_response('register.html',context_instance=RequestContext(request))