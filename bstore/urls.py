from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('cart/',views.cart,name='cart'),
    path('order/',views.order,name='order'),

    path('cart/<int:book_id>/',views.add_to_cart,name='add-cart'),
    path('cart/delete/<int:cart_id>/',views.delete_cart,name='cart-delete'),
    path('order/delete/<int:order_id>/',views.delete_order,name='order-delete'),

    path('profile/',views.profile,name='profile'),
    path('books/<slug:book_slug>/',views.book,name='product-book'),
    path('category/<slug:category_slug>/',views.home,name='home-by-category'),
    path('author/<slug:author_slug>/',views.home,name='home-by-author'),
    
]
