from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator
from forms import ProductForm
from models import Product

# Create your views here.

def create_product(request):
    form=ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=ProductForm()
    return render_to_response("create_product.html",context_instance=RequestContext(request))

def list_product(request):
    list_items=Product.objects.all()
    paginator=Paginator(list_items,10)
    try:
        page=int(request.GET.get('page',1))
    except ValueError:
        page=1

    try:
        list_items=paginator.page(page)
    except:
        list_items=paginator.page(paginator.num_pages)
    return render_to_response("list_product.html",context_instance=RequestContext(request))

def view_product(request,id):
    product_instance=Product.objects.get(id=id)
    return render_to_response("view_product.html",context_instance=RequestContext(request))

def edit_product(request,id):
    product_instance=Product.objects.get(id=id)
    form=ProductForm(request.POST or None,instance=product_instance)
    if form.is_valid():
        form.save()
    return render_to_response("edit_product.html",context_instance=RequestContext(request))