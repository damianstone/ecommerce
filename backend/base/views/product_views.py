from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from base.models import Product
from base.serializers import ProductSerializer
from rest_framework import status


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



