from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth.models import User



@api_view(['POST'])
def createUser(request):
    data = request.data

    # Check the password and confirm password
    if data['password'] != data['confirm_password']:
        raise Exception.ApiException('Passoword Did not matched')

    # Check if the email already exists 
    email = User.objects.get(email=data['email'])
    if email:
        raise Exception.ApiException('Email Already Exists')
   
    # Create the User    
    user = User.objects.create(
        first_name=data['first_name'],
        last_name=data['last_name'],
        username=data['email'],
        email=data['email'],
        password=make_password(data['password']),
    )
    # Response With Success Message
    return Response({'message':'user successfully created'}, status=status.HTTP_200_OK)

