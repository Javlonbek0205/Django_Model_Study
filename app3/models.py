from django.db import models
import datetime
# Create your models here.
"""Topshiriq 4: Uch Mavzuni Birlashtirish
Maqsad
Bu topshiriqda siz modellar yaratish, model methodlari, QuerySet methodlari va admin interfeysini moslashtirishni birlashtirgan holda to'liq bir loyiha yaratishingiz kerak bo'ladi.

Talablar
Qadam 1: Modellar Yaratish
Library va Book modellarini yarating.

Library modeli quyidagi fieldlardan iborat bo'lsin: name (CharField), location (CharField).
Book modeli quyidagi fieldlardan iborat bo'lsin: title (CharField), author (CharField), published_date (DateField), library (ForeignKey Library modeliga), genres (ManyToManyField Genre modeliga).
Genre modelini yarating.

Genre modeli quyidagi fieldlardan iborat bo'lsin: name (CharField).
Library modelining Meta sinfida quyidagi parametrlarni qo'shing:

ordering: name bo'yicha tartiblansin.
verbose_name: Library modelining nomini Kutubxona ga o'zgartiring.
verbose_name_plural: Libraries modelining ko'plik nomini Kutubxonalar ga o'zgartiring.
Har ikkala model uchun __str__ methodini qo'shing.

Qadam 2: Model Methods va QuerySet Methods
Book modelida save() methodini o'zgartiring: title va author fieldlaridagi harflarni bosh harfga aylantiring.

Library modelida custom method qo'shing: get_books_count(), bu method kutubxonadagi kitoblar sonini qaytarsin.

Book modelida custom method qo'shing: is_classic(), bu method kitob chop etilganiga 50 yil yoki undan ko'p bo'lgan bo'lsa True, aks holda False qaytarsin.

QuerySet methodlaridan foydalanib, Book modelidan barcha "Science Fiction" janridagi kitoblarni oling.

Qadam 3: Admin Interfeysini Moslashtirish va Inline Elements
Library modelini admin interfeysiga qo'shing va list_display parametrini name va location bilan moslang.

Genre modelini admin interfeysiga qo'shing.

Book modelini admin interfeysiga qo'shing.

Book modeli uchun Review modelini yarating: book (ForeignKey Book modeliga), review_text (TextField), rating (IntegerField), created_at (DateTimeField).

Review modelini Book modeliga inline sifatida qo'shing (TabularInline).

Admin interfeysida Book modelini moslashtiring: list_display (title, author, published_date, library), list_filter (published_date, genres), search_fields (title, author).

Yakuniy Ko'rsatmalar
Yaratilgan modellarni va methodlarni models.py fayliga kiriting.
Admin interfeysini moslashtirish uchun admin.py faylini tahrirlang.
Tushunarli qilib kommentariyalar yozib boring."""

class Library(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=250)
  class Meta:
    ordering = ['name']
    verbose_name = 'Kutubxona'
    verbose_name_plural = 'Kutubxonalar'
  def get_book_count(self):
    #Kitoblar sonini qaytaruvchi funksiya
    return  self.book_set.count()

  def __str__(self):
    return self.name


class Genre(models.Model):
  #kitobnni qaysi janrda ekanligini belgilaydi
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class BookQuerySet(models.QuerySet):
  def all_Science_Fiction(self):
    #Kitoblarni  'Science Fiction' janri bo`yicha filtrlaydi`
    return self.filter(genres__name='Science Fiction')

class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=150)
  published_date = models.DateField()
  library = models.ForeignKey(Library, on_delete=models.CASCADE)
  genres = models.ManyToManyField(Genre)

  def is_classic(self):
    #Kitobni classic yoki classic emasligini aniqlaydi
    current_year = datetime.date.today().year
    published_year = self.published_date.year
    return current_year-published_year>=50

  def save(self, *args, **kwargs):
    #kitobning title hamda authorini bosh harf bilan yozadi
    self.title = self.title.capitalize()
    self.author = self.author.title()
    super(Book, self).save(*args, **kwargs)

  objects = BookQuerySet.as_manager()

class Review(models.Model):
  book = models.ForeignKey(Book, on_delete = models.CASCADE)
  review_text = models.TextField()
  rating = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"Review for {self.book.title}"
