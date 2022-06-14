from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from base.serializers import ProductSerializer
from base.models import Product, Order, OrderItem, ShippingAddress

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_order_items(request):
    user = request.use # get the user
    data = request.data # get the data for the post request
    # all the order items sent in the post request
    order_items = data['order_items']
    
    # if there is no order items
    if order_items and len(order_items) == 0:
        return Response({'detail': 'No order items', status:status.HTTP_400_BAD_REQUEST})
    else:
        # 1-create order
        
        # 2-create shipping address
        
        # 3- create order items and set order to order item relationship 
        # => basically create the relation (forengh key) between the items and the whole order 
        
        
        # 4- update the count stock of products
        
        print('hola')
    
    return Response('ORDER')




