from rest_framework import serializers
from .models import User, Category, Product, Cart
from django.contrib.auth import authenticate


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'date_of_birth']
        read_only_fields = ['email'] 

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = (
            'id',
            'title'
        )
        model = Category 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'product_tag',
            'name',
            'category',
            'price',
            'stock',
            'image',
            'created_by',
            'status',
            'date_created'
        )
        model = Product
        read_only_fields = ('created_by',)

class UserSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'products',
        )

class CartUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'email')

class CartSerializer(serializers.ModelSerializer):
    cart_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  # for POST
    products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)

    class Meta:
        model = Cart
        fields = ('cart_id', 'created_at', 'products')

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password_confirm']
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("Passwords don't match")
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

