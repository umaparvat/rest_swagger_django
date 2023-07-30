from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializer import ProductSerializer
from .models import Product
# Create your views here.

class ProductApi(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
