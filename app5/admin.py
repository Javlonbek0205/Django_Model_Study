from django.contrib import admin
from .models import Product, Category, Customer, Order
# Register your models here.
"""Django Admin Panelini Moslashtirish:

ProductAdmin klassini yarating va list_display, list_filter, search_fields ni sozlang:

list_display: name, price, stock.
list_filter: price, stock.
search_fields: name.
CategoryAdmin klassini yarating va list_display, search_fields ni sozlang:

list_display: name.
search_fields: name.
OrderAdmin klassini yarating va list_display, list_filter, search_fields ni sozlang:

list_display: customer_name, order_date.
list_filter: order_date.
search_fields: customer_name."""
class ProductAdmin(admin.ModelAdmin):
  list_display = ['name', 'price', 'stock']
  list_filter = ['name', 'stock',]
  search_fields = ('name',)

class CategoryAdmin(admin.ModelAdmin):
  list_display = ['name']
  search_fields = ('name',)

class OrderAdmin(admin.ModelAdmin):
  list_display = ['customer_name', 'order_date']
  list_filter = ['order_date',]
  search_fields = ('customer_name',)

admin.site.register(Customer)
admin.site.register(Order, OrderAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)