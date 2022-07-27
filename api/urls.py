from django.urls import path
from .views import createUser


urlpatterns =[
    path('accounts/create_user/',createUser),
]