
from rest_framework import serializers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


from rest_framework_simplejwt.tokens import RefreshToken


from warehouse.models import Product, Category, Company
from accounts.models import CustomUser


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name']


class UserSerializerWithToken(serializers.ModelSerializer):
    access_token = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'access_token']
    
    def get_access_token(self, user):
        token = RefreshToken.for_user(user)
        return str(token.access_token)


class ProductsSerializer(serializers.ModelSerializer):
    product_category = serializers.SerializerMethodField(read_only=True)
    product_company = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'

    def get_product_category(self, obj):
        category = obj.category
        serializer = CategorySerializer(category, many=False)
        return serializer.data
    def get_product_company(self, obj):
        company = obj.company
        serializer = CompanySerializer(company, many=False)
        return serializer.data

