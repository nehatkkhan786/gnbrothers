from django.urls import path
from .views import createUser, ProducView, MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns =[
    path('accounts/create_user/',createUser),
    path('products/', ProducView.as_view()),
     path('account/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('account/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]