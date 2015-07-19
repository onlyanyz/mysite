from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator
from forms import ProductForm
from models import Product,Cart,LineItem
import datetime
from rest_framework import viewsets
from serializers import LineItemSerializer

# Create your views here.

def create_product(request):
    form=ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=ProductForm()
    return render_to_response("create_product.html",locals(),context_instance=RequestContext(request))

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
    return render_to_response("list_product.html",locals(),context_instance=RequestContext(request))

def view_product(request,id):
    product_instance=Product.objects.get(id=id)
    return render_to_response("view_product.html",context_instance=RequestContext(request))

def edit_product(request,id):
    product_instance=Product.objects.get(id=id)
    form=ProductForm(request.POST or None,instance=product_instance)
    if form.is_valid():
        form.save()
    return render_to_response("edit_product.html",context_instance=RequestContext(request))

def store_view(request):
    products=Product.objects.filter(date_available__gt=datetime.datetime.now().date()).order_by("-date_available")
    return render_to_response("store.html",locals(),context_instance=RequestContext(request))

def view_cart(request):
    cart=request.session.get("cart",None)
    if not cart:
        cart=Cart()
        request.session["cart"]=cart
    return render_to_response("view_cart.html",locals(),context_instance=RequestContext(request))

def add_to_cart(request,id):
    product=Product.objects.get(id=id)
    cart=request.session.get("cart",None)
    if not cart:
        cart=Cart()
        request.session["cart"]=cart
    cart.add_product(product)
    request.session["cart"]=cart
    return view_cart(request)

def clean_cart(request):
    request.session["cart"]=Cart()
    return view_cart(request)

class LineItemViewSet(viewsets.ModelViewSet):
    queryset = LineItem.objects.all()
    serializer_class = LineItemSerializer