#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
import datetime
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import View

from serializers import LineItemSerializer,ProductSerializer
from forms import ProductForm
from models import Product,Cart,LineItem

# Create your views here.

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

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
    return render_to_response("view_product.html",locals(),context_instance=RequestContext(request))

def edit_product(request,id):
    product_instance=Product.objects.get(id=id)
    form=ProductForm(request.POST or None,instance=product_instance)
    if form.is_valid():
        form.save()
    return render_to_response("edit_product.html",locals(),context_instance=RequestContext(request))

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

# class LineItemViewSet(viewsets.ModelViewSet):
#     queryset = LineItem.objects.all()
#     serializer_class = LineItemSerializer

# class RESTforCart(View):
#     def get(self,request,*args,**kwargs):
#         return request.session['cart'].items

@api_view(['GET','POST'])
def cart_item_list(request):
    # if request.method=='GET':
    #     try:
    #         lineitem=LineItem.objects.all()
    #     except LineItem.DoesNotExist:
    #         return HttpResponse(status=404)
    #     serializer=LineItemSerializer(lineitem,many=True)
    #     return JSONResponse(serializer.data)
    # elif request.method=='POST':
    #     if not request.DATA:
    #         errors={"errno":"-1","errmsg":"请求参数错误"}
    #         return JSONResponse(errors,status=200)
    #     serializer=LineItemSerializer(data=request.DATA,many=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method=='GET':
        # return JSONResponse(request.session['cart'].items)
        return JSONResponse({"errno":"-1","errmsg":"请求参数错误"})

@api_view(['GET',])
def product_list(request):
    if request.method=='GET':
        # if request.GET.has_key('pid'):
        #     if request.GET['pid']<=0:
        #         errors={"errno":"-1","errmsg":"请求参数错误"}
        #         return JSONResponse(errors,status=200)
        #     else:
        #         try:
        #             product=Product.objects.get(id=pid)
        #         except Product.DoesNotExist:
        #             return HttpResponse(status=404)
        #         serializer=ProductSerializer(product,many=True)
        if not request.GET.has_key('pid'):
            try:
                product=Product.objects.all()
            except Product.DoesNotExist:
                return HttpResponse(status=404)
            serializer=ProductSerializer(product,many=True)
        return JSONResponse(serializer.data)
