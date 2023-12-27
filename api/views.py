from rest_framework import generics, status
from rest_framework.response import Response
from .models import *
from django.contrib.auth.models import User
from .serializers import *
from rest_framework.permissions import IsAuthenticated 
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi



#Author 
class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['slug', 'id']
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def get(self, request, *args, **kwargs):
        try:
            response = super().get(request, *args, **kwargs)
            return Response(response.data, status=response.status_code)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            return Response(response.data, status=response.status_code)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes=[IsAuthenticated]
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def get(self, request, *args, **kwargs):
        try:
            response = super().get(request, *args, **kwargs)
            return Response(response.data, status=response.status_code)
        except Exception as e:
            Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def put(self, request, *args, **kwargs):
        try:
            response = super().put(request, *args, **kwargs)
            return Response(response.data, status=response.status_code)
        except Exception as e:
            Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def patch(self, request, *args, **kwargs):
        try:
            response = super().patch(request, *args, **kwargs)
            return Response(response.data, status=response.status_code)
        except Exception as e:
            Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def delete(self, request, *args, **kwargs):
        try:
            response = super().delete(request, *args, **kwargs)
            return Response(response.data, status=response.status_code)
        except Exception as e:
            Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#Category
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['slug','id']
    permission_classes=[IsAuthenticated]
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def get(self, request, *args, **kwargs):
        try:
            response = super().get(request, *args, **kwargs)
            return Response(response.data, status=response.status_code)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            return Response(response.data, status=response.status_code)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes=[IsAuthenticated]
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def get(self, request, *args, **kwargs):
        try:
            response = super().get(request, *args, **kwargs)
            return Response(response.data, status=response.status_code)
        except Exception as e:
            Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def put(self, request, *args, **kwargs):
        try:
            response = super().put(request, *args, **kwargs)
            return Response(response.data, status=response.status_code)
        except Exception as e:
            Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def patch(self, request, *args, **kwargs):
        try:
            response = super().patch(request, *args, **kwargs)
            return Response(response.data, status=response.status_code)
        except Exception as e:
            Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def delete(self, request, *args, **kwargs):
        try:
            response = super().delete(request, *args, **kwargs)
            return Response(response.data, status=response.status_code)
        except Exception as e:
            Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

#Book
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id','slug','categories__slug','author__slug']
    permission_classes=[IsAuthenticated]
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def get(self, request, *args, **kwargs):
            try:
                response = super().get(request, *args, **kwargs)
                for item in response.data:
                    if 'cover_image' in item and item['cover_image']:
                        item['cover_image'] = item['cover_image'].replace('http://127.0.0.1:8000', '')

                return Response(response.data, status=response.status_code)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            return Response(response.data, status=response.status_code)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes=[IsAuthenticated]
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def get(self, request, *args, **kwargs):
        try:
            response = super().get(request, *args, **kwargs)
            response_data = response.data
            response_data['cover_image'] = response_data['cover_image'].replace('http://127.0.0.1:8000', '')
            return Response(response_data, status=response.status_code)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def put(self, request, *args, **kwargs):
        try:
            response = super().put(request, *args, **kwargs)
            return Response(response.data, status=response.status_code)
        except Exception as e:
            Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def patch(self, request, *args, **kwargs):
        try:
            response = super().patch(request, *args, **kwargs)
            return Response(response.data, status=response.status_code)
        except Exception as e:
            Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def delete(self, request, *args, **kwargs):
        try:
            response = super().delete(request, *args, **kwargs)
            return Response(response.data, status=response.status_code)
        except Exception as e:
            Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#user
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes=[IsAuthenticated]
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def get(self, request, *args, **kwargs):
        try:
            response = super().get(request, *args, **kwargs)
            return Response(response.data, status=response.status_code)
        except Exception as e:
            Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def put(self, request, *args, **kwargs):
        try:
            response = super().put(request, *args, **kwargs)
            return Response(response.data, status=response.status_code)
        except Exception as e:
            Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def patch(self, request, *args, **kwargs):
        try:
            response = super().patch(request, *args, **kwargs)
            return Response(response.data, status=response.status_code)
        except Exception as e:
            Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def delete(self, request, *args, **kwargs):
        try:
            response = super().delete(request, *args, **kwargs)
            return Response(response.data, status=response.status_code)
        except Exception as e:
            Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#cart
class CartItemList(generics.ListCreateAPIView):
    
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['cart_user__id',]
    permission_classes=[IsAuthenticated]
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def get(self, request, *args, **kwargs):
        try:
            response = super().get(request, *args, **kwargs)
            return Response(response.data, status=response.status_code)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            return Response(response.data, status=response.status_code)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class CartItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes=[IsAuthenticated]
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def get(self, request, *args, **kwargs):
        try:
            response = super().get(request, *args, **kwargs)
            return Response(response.data, status=response.status_code)
        except Exception as e:
            Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def put(self, request, *args, **kwargs):
        try:
            response = super().put(request, *args, **kwargs)
            return Response(response.data, status=response.status_code)
        except Exception as e:
            Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def patch(self, request, *args, **kwargs):
        try:
            response = super().patch(request, *args, **kwargs)
            return Response(response.data, status=response.status_code)
        except Exception as e:
            Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def delete(self, request, *args, **kwargs):
        try:
            response = super().delete(request, *args, **kwargs)
            return Response(response.data, status=response.status_code)
        except Exception as e:
            Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#order
class OrderItemList(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['order_user__id',]
    permission_classes=[IsAuthenticated]
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def get(self, request, *args, **kwargs):
        try:
            response = super().get(request, *args, **kwargs)
            return Response(response.data, status=response.status_code)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            return Response(response.data, status=response.status_code)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class OrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes=[IsAuthenticated]
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def get(self, request, *args, **kwargs):
        try:
            response = super().get(request, *args, **kwargs)
            return Response(response.data, status=response.status_code)
        except Exception as e:
            Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def put(self, request, *args, **kwargs):
        try:
            response = super().put(request, *args, **kwargs)
            return Response(response.data, status=response.status_code)
        except Exception as e:
            Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def patch(self, request, *args, **kwargs):
        try:
            response = super().patch(request, *args, **kwargs)
            return Response(response.data, status=response.status_code)
        except Exception as e:
            Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description='Token <your_access_token>',
                required=True,
            ),
        ],
    )
    def delete(self, request, *args, **kwargs):
        try:
            response = super().delete(request, *args, **kwargs)
            return Response(response.data, status=response.status_code)
        except Exception as e:
            Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CustomAuthTokenLogin(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'username': user.username,
            'token': f"Token {token.key}",
            
        })



