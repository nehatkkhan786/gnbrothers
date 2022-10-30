

# Rest Framework Import 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



# Django Default Imports
from django.contrib.auth.models import User


# Local Imports
from .serializers import ProductsSerializer
from .serializers import UserSerializerWithToken
from warehouse.models import Product, Category, Company
from accounts.models import CustomUser



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data
        print(serializer)
        return serializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['POST'])
def createUser(request):
    data = request.data

    # Check the password and confirm password
    if data['password'] != data['confirm_password']:
        raise Exception.ApiException('Passoword Did not matched')

    # Check if the email already exists 
    email = CustomUser.objects.filter(email=data['email']).exists()
    if email:
        raise Exception.ApiException('Email Already Exists')
   
    # Create the User    
    user = CustomUser.objects.create_user(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        password=(data['password']),
    )
    serializer = UserSerializerWithToken(user, many=False)
    # Response With Success Message
    return Response(serializer.data, status=status.HTTP_200_OK)


class ProducView(APIView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductsSerializer(products, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)