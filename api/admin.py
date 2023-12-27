from django.contrib import admin

from .models import Category, Author, Book,CartItem, OrderItem
# Register your models here.

admin.site.register(Author)

admin.site.register(Category)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','categories','published_date','price')
admin.site.register(Book,BookAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display = ('book','cart_user','quantity','date_added','slug')
admin.site.register(CartItem,CartAdmin)



class OrderAdmin(admin.ModelAdmin):
    list_display = ('book','order_user','quantity','date_added')
admin.site.register(OrderItem,OrderAdmin)
