from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from base.serializers import ProductSerializer, UserSerializer, UserSerializerWithToken

# simple json token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# hash the password
from django.contrib.auth.hashers import make_password
from rest_framework import status


# TOKEN SERIALIZER
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        
        """
        se puede hacer de la siguinte manera (de forma manual) 
            data['username'] = self.user.username
            data['email'] = self.user.email
            
            O se puede hacer mediante un for loop usando el serializer cn el token
        """
        
        serializer = UserSerializerWithToken(self.user).data
        for key, value in serializer.items():
            data[key] = value
    
        return data

# TOKEN VIEW
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def registerUser(request):
    # get the data sent from frontend
    data = request.data
    # dont allow users creations with the same data
    try: 
        # create a new user data model
        user = User.objects.create(
            first_name = data['name'],
            username = data['email'],
            email = data['email'],
            password = make_password(data['password']) # store the password as a hash 
        )
        # serialize with the token one to then automatically create the auth and refresh token for the new user
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'User with this email already exist'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated]) # IsAuth => the user needs to be authenticated to access this view 
def getUserProfile(request):
    user = request.user # need to receive the token in the headers to return the profile info
    serializer = UserSerializer(user, many=False)
    # return the user object including info like the personal token, email, username, etc
    return Response(serializer.data)



@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserProfile(request):
    user = request.user 
    serializer = UserSerializerWithToken(user, many=False)
    
    data = request.data
    user.first_name = data['name']
    user.username = data['email']
    user.email = data['email']
     
    # just if the password is not blank (so its optional)
    if data['password'] != '':
        user.password = make_password(data['password'])
    
    user.save()
            
    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([IsAdminUser]) # this view is just for the admins (developers for example) 
def getUsers(request):
    # get all the users from the db
    users = User.objects.all()
    serializer = UserSerializerWithToken(users, many=True)
    return Response(serializer.data)






