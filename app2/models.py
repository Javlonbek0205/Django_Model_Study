from django.db import models

# Create your models here.
"""Topshiriq 1: Custom Model Methods va QuerySet Methods
Maqsad
Bu topshiriqda siz custom model methodlar va QuerySet methodlarini o'zlashtirishingiz kerak.

Talablar
Movie va Director modellarini yarating.
Movie modeli quyidagi fieldlardan iborat bo'lsin: title (CharField), release_date (DateField), director (ForeignKey Director modeliga).
Director modeli quyidagi fieldlardan iborat bo'lsin: first_name (CharField), last_name (CharField).
Director modelida custom method qo'shing: full_name(), bu method first_name va last_name ni birlashtirib to'liq ismni qaytarsin.
Movie modelida custom method qo'shing: is_recent(), bu method filmlar hozirgi sanadan 5 yil ichida chiqqan bo'lsa True, aks holda False qaytarsin.
QuerySet methodlaridan foydalanib, Movie modelidan barcha 2020 yildan keyin chiqarilgan filmlarni oling."""
import datetime
class MovieQuerySet(models.QuerySet):
  def release_2020(self):
    return self.filter(release_date__year__gte=2020)
class Director(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  def full_name(self):
    return f"{self.first_name.title()} {self.last_name.title()}"
class Movie(models.Model):
  title = models.CharField(max_length=200)
  release_date = models.DateField()
  director = models.ForeignKey(Director, on_delete=models.CASCADE)
  def is_recent(self):
    current_year = datetime.date.today().year
    release_year = self.release_date.year
    return (current_year - release_year) <= 5
  objects = MovieQuerySet.as_manager()

#--------------------------------------------------------------------------------------

"""Topshiriq 2: Model Administratsiyasi va Inline Elements
Maqsad
Bu topshiriqda siz Django admin interfeysini moslashtirishingiz, modellarga inlinelar qo'shishingiz va admin interfeysida fieldlarni moslashtirishingiz kerak.

Talablar
Author va BlogPost modellarini yarating.
Author modeli quyidagi fieldlardan iborat bo'lsin: first_name (CharField), last_name (CharField), email (EmailField).
BlogPost modeli quyidagi fieldlardan iborat bo'lsin: title (CharField), content (TextField), author (ForeignKey Author modeliga), published_date (DateTimeField).
Author modelini admin interfeysiga qo'shing va list_display parametrini first_name, last_name, va email bilan moslang.
BlogPost modelini admin interfeysiga qo'shing.
BlogPost modeli uchun Comment modelini yarating: blogpost (ForeignKey BlogPost modeliga), text (TextField), created_at (DateTimeField).
Comment modelini BlogPost modeliga inline sifatida qo'shing (StackedInline).
Admin interfeysida BlogPost modelini moslashtiring: list_display (title, author, published_date), list_filter (published_date), search_fields (title, content)."""
class Author(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.EmailField()

  def __str__(self):
        return f"{self.first_name} {self.last_name}"

class BlogPost(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField()
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  published_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
        return self.title

class Comment(models.Model):
  blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
  text = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
        return self.text[:50]
#-----------------------------------------------------------------------------------------

"""Topshiriq 3: Model Meta Options
Maqsad
Bu topshiriqda siz modellarda Meta sinfidan foydalanib, ordering va verbose name kabi imkoniyatlarni qo'llashingiz kerak.

Talablar
Course va Student modellarini yarating.
Course modeli quyidagi fieldlardan iborat bo'lsin: name (CharField), code (CharField).
Student modeli quyidagi fieldlardan iborat bo'lsin: first_name (CharField), last_name (CharField), enrolled_courses (ManyToManyField Course modeliga).
Course modelining Meta sinfida quyidagi parametrlarni qo'shing:
ordering: name bo'yicha tartiblansin.
verbose_name: Course modelining nomini Kurs ga o'zgartiring.
verbose_name_plural: Courses modelining ko'plik nomini Kurslar ga o'zgartiring.
Student modelining Meta sinfida quyidagi parametrlarni qo'shing:
ordering: last_name va first_name bo'yicha tartiblansin.
verbose_name: Student modelining nomini Talaba ga o'zgartiring.
verbose_name_plural: Students modelining ko'plik nomini Talabalar ga o'zgartiring."""
class Courses(models.Model):
   name = models.CharField(max_length=200)
   code = models.CharField(max_length=250)
   class Meta:
      ordering = ['name']
      verbose_name = 'Kurs'
      verbose_name_plural = 'Kurslar'

   def __str__(self):
    return self.name

class Student(models.Model):
   first_name = models.CharField(max_length=100)
   last_name = models.CharField(max_length=100)
   enrolled_courses = models.ManyToManyField(Courses)

   class Meta:
      ordering = ['last_name', 'first_name']
      verbose_name = 'Talaba'
      verbose_name_plural = 'Talabalar'

   def __str__(self):
      return f"{self.first_name} {self.last_name}"
#----------------------------------------------------------------------------------------------------