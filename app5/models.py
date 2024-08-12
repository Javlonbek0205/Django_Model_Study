from django.db import models
from django.db.models import Sum
# Create your models here.
"""2-Topshiriq: Onlayn Magazin
Ma'lumotlar Modellarini Yaratish:

Product modeli:

name (CharField): Mahsulot nomi.
price (DecimalField): Mahsulot narxi.
stock (IntegerField): Mahsulotning mavjud miqdori.
Meta sinfidan foydalanib ordering ni price bo‘yicha sozlang.
Category modeli:

name (CharField): Kategoriyaning nomi.
description (TextField): Kategoriyaning qisqacha tavsifi.
products (ManyToManyField): Ushbu kategoriyaga tegishli mahsulotlar.
Custom Method: Ushbu kategoriyaga tegishli jami mahsulotlar sonini qaytaruvchi method yozing (get_total_products).
Order modeli:

customer_name (CharField): Mijozning ismi.
order_date (DateTimeField): Buyurtma sanasi.
products (ManyToManyField): Buyurtma qilingan mahsulotlar.
Custom Method: Buyurtma qilingan mahsulotlarning jami narxini hisoblovchi method yozing (calculate_total_price).
Customer modeli:

first_name (CharField): Mijozning ismi.
last_name (CharField): Mijozning familiyasi.
email (EmailField): Mijozning email manzili.
orders (ForeignKey): Mijozning qaysi buyurtmalari mavjudligini belgilash.
Miqyoslash, Customization va Advanced ORM Queries:

Aggregation: Har bir buyurtma uchun jami mahsulot sonini va jami narxni annotate yordamida hisoblang.
ORM Queries: select_related va prefetch_related yordamida buyurtmalar va ularga tegishli mahsulotlarni, mijozlar bilan birga yuklang.
Custom Manager Method: Order modeli uchun recent_orders methodini yarating, u so‘nggi 30 kun ichidagi buyurtmalarni qaytarsin.
Django Admin Panelini Moslashtirish:

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
search_fields: customer_name.
Migrationlar:

Barcha modellaringiz uchun makemigrations va migrate buyruqlarini ishlating."""
import datetime
class Product(models.Model):
  name = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  stock = models.IntegerField()
  class Meta:
    ordering = ['price']

  def __str__(self):
    return self.name

class Category(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  products = models.ManyToManyField(Product)

  def get_total_products(self):
    return self.products.count()

  def  __str__(self):
    return self.name

class Order(models.Model):
  customer_name = models.CharField(max_length=150)
  order_date = models.DateTimeField(auto_now_add=True)
  products = models.ManyToManyField(Product)

  def calculate_total_price(self):
    return  self.products.aggregate(total = Sum('price'))['total']

  def recent_orders(self):
    current_day = datetime.datetime.now().date
    return self.objects.filter(order_date__gte = current_day-datetime.timedelta(days=30))

  def  __str__(self):
    return f"{self.customer_name} products: {', '.join([product.name for product in self.products.all()])}"

class Customer(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.EmailField()
  orders = models.ForeignKey(Order, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"

# QuerySet examples (These would be in your view or shell, not in the models.py):
# total_price = Order.objects.aggregate(Sum('products__price'))
# total_count = Order.objects.annotate(product_count=Count('products'))
# orders = Order.objects.select_related('products').all()