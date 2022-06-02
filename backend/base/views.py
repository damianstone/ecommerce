from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .products import products
from .serializers import ProductSerializer

# Create your views here.

# use functions instead of classes for the views
# is the same thing but with function you have more control of what u are doing


# write the mtohods we gonna allow
@api_view(['GET'])
def getRoutes(request):
    routes = [
    '/api/products/',
    '/api/products/create/',

    'api/products/upload/',

    'api/products/<id>/reviews/',

    'api/products/top/',
    'api/products/<id>/',

    'api/products/delete/<id>/',
    'api/products/<update>/<id>/',

    ]
    return Response(routes)


@api_view(['GET'])
def getProducts(request):
    #.all return all of the product from our database
    # before to push data to the frontend we have to serialize the data
    products = Product.objects.all() #query
    serializer = ProductSerializer(products, many=True) # many = multiple objetcs 
    return Response(serializer.data)

# pk = id
@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)
