from django.urls import path
from .views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="akrn BookStore API",
        default_version='v1',
        description="List of APIs used in BookStore",
        terms_of_service="https://www.akrnbookstore.com/terms/",
        contact=openapi.Contact(email="contact@akrnbookstore.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    
)


urlpatterns = [
    path('login/',CustomAuthTokenLogin.as_view(),name='get-token'),
    path('authors/', AuthorList.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('cartitems/', CartItemList.as_view(), name='cartitems-list'),
    path('cartitems/<int:pk>/', CartItemDetail.as_view(), name='cartitems-detail'),
    path('orderitems/', OrderItemList.as_view(), name='orderitems-list'),
    path('orderitems/<int:pk>/', OrderItemDetail.as_view(), name='orderitems-detail'),
    
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


]