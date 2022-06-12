from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Product 


# transform data into json 
# return las propiedades especificadas en fields cuando se llama 
class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = User 
        # fields we want to return when we make a request of the user profiles
        fields = ['_id', 'username', 'email', 'name', 'isAdmin']
    
    def get__id(self, obj):
        return obj.id
    
    def get_isAdmin(self, obj):
        return obj.is_staff
        
    # parameter: the serializer and the user object
    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email
            
        return name

# se pasa como parametro el el otro serializer asi este serializer es solo
# una extencion del otro, el cual contiene las mismas propiedades que UserSerializer + token
class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = User
        fields = ['_id', 'username', 'email', 'name', 'isAdmin', 'token']
    
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token)
        
        
# transform data into json 
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = '__all__'



