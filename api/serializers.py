from rest_framework import serializers
from .models import Author, Category, Book, CartItem, OrderItem
from django.contrib.auth.models import User

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name','slug',]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name','slug',]

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'categories', 'published_date', 'price', 'description','cover_image','slug','in_cart',]

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField( write_only=True, required=False)
    username = serializers.CharField(read_only=True, required=False)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')

    def update(self, instance, validated_data):
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)
            validated_data['password']=instance.password
            # print(instance.password)
            # print(validated_data['password'])

        return super().update(instance, validated_data)

class CartItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CartItem
        fields = ['id','book', 'cart_user', 'quantity',  'slug',]


class OrderItemSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = OrderItem
        fields = ['id','book', 'order_user', 'quantity',]




