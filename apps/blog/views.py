from django.shortcuts import render
from django.shortcuts import  render_to_response
from django.template import RequestContext
from models import BlogPost

# Create your views here.

def home(request):
    posts=BlogPost.objects.all()
    return render_to_response("bloglist.html",{'blogs':posts},context_instance=RequestContext(request))
