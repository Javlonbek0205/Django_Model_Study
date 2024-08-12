from django.db import models
from django.db.models import Q
# Create your models here.
"""Topshiriq 1: Oddiy Model Yaratish
Talablar:
Student nomli model yarating.
Quyidagi maydonlarni qo'shing:
first_name (CharField, maksimal uzunlik 50 ta belgi)
last_name (CharField, maksimal uzunlik 50 ta belgi)
age (IntegerField)"""
class Student(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  age = models.IntegerField()
#-----------------------------------------------------------------------------------------
"""Topshiriq 2: Abstrakt Model Yaratish
Talablar:
Person nomli abstrakt model yarating.
Quyidagi maydonlarni qo'shing:
name (CharField, maksimal uzunlik 100 ta belgi)
email (EmailField)
Teacher va Student modellarini Person modelidan meros qilib oling va qo'shimcha maydonlarni qo'shing:
Teacher modeliga subject (CharField, maksimal uzunlik 100 ta belgi)
Student modeliga grade (CharField, maksimal uzunlik 10 ta belgi)"""
class Person(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  class Meta:
    abstract = True
class Teacher(Person):
  subject = models.CharField(max_length=100)
class Custom_Student(Person):
  grade = models.CharField(max_length=10)

"""Topshiriq 3: Meta Sinfi Bilan Model Yaratish
Talablar:
Course nomli model yarating.
Quyidagi maydonlarni qo'shing:
title (CharField, maksimal uzunlik 100 ta belgi)
description (TextField)
start_date (DateField)
end_date (DateField)
Meta sinfida quyidagi sozlamalarni qo'shing:
Model courses nomli jadvalga saqlansin (db_table).
Ma'lumotlar start_date bo'yicha tartiblanadi (ordering).
Admin panelda model nomi "Course Information" bo'lsin (verbose_name).
Admin panelda modelning ko'plik shaklidagi nomi "Course Information" bo'lsin (verbose_name_plural)."""
class Course(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  start_date = models.DateField()
  end_date = models.DateField()
  class Meta:
    db_table = 'courses'
    ordering = ['start_date']
    verbose_name = 'Course Iinformation'
    verbose_name_plural = 'Course Information'

#------------------------------------------------------------------------------------

"""Topshiriq 4: Unique Constraints va Indexes
Talablar:
Enrollment nomli model yarating.
Quyidagi maydonlarni qo'shing:
student (ForeignKey, Student modeliga ishora qiladi)
course (ForeignKey, Course modeliga ishora qiladi)
enrollment_date (DateField)
Meta sinfida quyidagi sozlamalarni qo'shing:
student va course maydonlari yagona kombinatsiya bo'lsin (unique_together).
student va enrollment_date maydonlari uchun indeks yarating (index_together)."""
class Enrollment(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  course = models.ForeignKey(Course, on_delete=models.CASCADE)
  enrollment_date = models.DateField()
  class Meta:
    unique_together = ['student', 'course']
    index_together = ['student', 'enrollment_date']

#------------------------------------------------------------------------------

"""Topshiriq 5: Qo'shimcha Cheklovlar
Talablar:
Event nomli model yarating.
Quyidagi maydonlarni qo'shing:
name (CharField, maksimal uzunlik 100 ta belgi)
location (CharField, maksimal uzunlik 100 ta belgi)
start_time (DateTimeField)
end_time (DateTimeField)
Meta sinfida quyidagi sozlamalarni qo'shing:
start_time end_timedan oldinroq bo'lishi kerak (constraints)."""
class Event(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()
  class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(start_time__lt = 'end_time'),
                name='check_start_time_before_end_time'
            )
        ]
#---------------------------------------------------------------------------------
"""1-topshiriq: save() metodini o'zgartirish
Vazifa:

Person nomli model yaratish, quyidagi maydonlar bilan:
first_name - CharField(max_length=50)
last_name - CharField(max_length=50)
age - IntegerField()
save() metodini o'zgartirish, quyidagi shartlar bilan:
age qiymati manfiy bo'lmasligi kerak, agar manfiy bo'lsa, ValueError chiqarilishi kerak.
first_name va last_name maydonlarini bosh harf bilan yozish (capitalize qilish)."""

class CustomPerson(models.Model):
  first_name = models.CharField(max_length = 50)
  last_name = models.CharField(max_length = 50)
  age = models.IntegerField()

  def save(self, *args, **kwargs):
    self.first_name = self.first_name.capitalize()
    self.last_name = self.last_name.capitalize()
    if self.age<0:
      raise ValueError("Yosh manfiy bo`lmaydi")
    super(CustomPerson, self).save(*args, **kwargs)

# Person obyektini yaratish va saqlash
"""person = Person(first_name='javlonbek', last_name='ibrahimov', age=25)
person.save()
print(person.first_name)  # Javlonbek
print(person.last_name)   # Ibrahimov

# Xato chiqarish
try:
    invalid_person = Person(first_name='ali', last_name='valiyev', age=-5)
    invalid_person.save()
except ValueError as e:
    print(e)  # Yosh manfiy bo'lmaydi
"""

#---------------------------------------------------------------------------------
"""2-topshiriq: Custom metodlar qo'shish
Vazifa:

Book nomli model yaratish, quyidagi maydonlar bilan:
title - CharField(max_length=100)
author - CharField(max_length=100)
published_year - IntegerField()
Book modelida quyidagi custom metodlarni qo'shing:
get_book_info(): Kitob nomi va muallifini qaytaradi, masalan, "Title by Author".
is_classic(): Kitob 50 yildan ko'p avval nashr etilgan bo'lsa, True qaytaradi."""
import datetime
class Book(models.Model):
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  published_year = models.IntegerField()
  def get_book_info(self):
    return f"{self.title} by {self.author}"

  def is_classic(self):
    current_year = datetime.datetime.now().year
    return   current_year- self.published_year>50

# Book obyektini yaratish va saqlash
"""book = Book(title='The Great Gatsby', author='F. Scott Fitzgerald', published_year=1925)
book.save()
print(book.get_book_info())  # The Great Gatsby by F. Scott Fitzgerald
print(book.is_classic())     # True
"""
#--------------------------------------------------------------------------------------
#-->1-CharField: Qisqa matn uchun ishlatiladi. Maksimal uzunlikni belgilash kerak.
#name = models.CharField(max_length=100)

#-->2-TextField: Katta matn uchun ishlatiladi. Maxsus uzunlikni belgilash shart emas.
#description = models.TextField()

#-->3-IntegerField: Butun sonlar uchun.
#age = models.IntegerField()

#-->4-PositiveIntegerField: Musbat butun sonlar uchun.
#age = models.PositiveIntegerField()

#-->5-FloatField: Qaytariladigan raqamlar uchun.
#price = models.FloatField()

#-->6-DecimalField: O'nlik raqamlar uchun. Aniqlik va o'lchovlarni belgilash mumkin.
#price = models.DecimalField(max_digits=10, decimal_places=2)

#-->7-BooleanField: Ha/Yo'q qiymatlar uchun
#is_active = models.BooleanField(default=True)

#-->8-DateField: Sana uchun.
#birth_date = models.DateField()

#-->9-DateTimeField: Sana va vaqt uchun.
#created_at = models.DateTimeField(auto_now_add=True)

#-->10-TimeField: Faqat vaqt uchun.
#appointment_time = models.TimeField()

#-->11-FileField: Fayl yuklash uchun. upload_to parametrini ko'rsatish kerak.
#document = models.FileField(upload_to='documents/')

#-->12-ImageField: Rasm yuklash uchun. upload_to parametrini ko'rsatish kerak.
#image = models.ImageField(upload_to='images/')

#-->13-ForeignKey: Boshqa modelga bog'lanishni belgilaydi (bir-birga bog'liq ma'lumotlar).
#class Author(models.Model):
#    name = models.CharField(max_length=100)
#class Book(models.Model):
#    title = models.CharField(max_length=200)
#    author = models.ForeignKey(Author, on_delete=models.CASCADE)

#-->14-ManyToManyField: Ko'p-ko'p bog'lanishni belgilaydi (ko'p obyektlarning ko'p obyektlar bilan bog'lanishi).
#class Author(models.Model):
#    name = models.CharField(max_length=100)
#class Book(models.Model):
#    title = models.CharField(max_length=200)
#    authors = models.ManyToManyField(Author)

#-->15-OneToOneField: Har bir obyekt faqat bitta boshqa obyekt bilan bog'lanishini belgilaydi.
#from django.contrib.auth.models import User
#class UserProfile(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    bio = models.TextField()



#--------------------------------------------------------------------------------------------

#-->1-abstract: Bu parametr modelning abstrakt model ekanligini belgilaydi. Abstrakt modeldan meros olgan boshqa modellar ma'lumotlar bazasida jadval yaratadi, lekin o'zi uchun jadval yaratmaydi.
"""class Meta:
    abstract = True"""

#-->2-app_label: Model qaysi ilovaga (app) tegishli ekanligini belgilaydi. Bu parametr faqat noyob hollarda, model fayllari odatiy joylashuvidan boshqa joyga ko'chirilganda ishlatiladi.
"""class Meta:
    app_label = 'my_app'"""

#-->3-base_manager_name: Model uchun asosiy menejer (manager) nomini belgilaydi. Default bo'yicha bu "objects" menejeridir.
"""class Meta:
    base_manager_name = 'custom_manager'"""

#-->4-default_manager_name: Model uchun default menejer nomini belgilaydi.
"""class Meta:
    default_manager_name = 'custom_manager'"""

#-->5-db_tablespace: Modelning indekslari uchun ma'lumotlar bazasidagi tablespace'ni belgilaydi.
"""class Meta:
    db_tablespace = 'my_tablespace'"""

#-->6-default_related_name: Ushbu modelga oid bo'lgan barcha ForeignKey yoki OneToOneField uchun default related name ni belgilaydi.
"""class Meta:
    default_related_name = 'my_related_name'"""

#-->7-get_latest_by: Modelning latest() metodidan foydalanilganda qaysi maydon bo'yicha eng so'nggi yozuvni olish kerakligini belgilaydi.
"""class Meta:
    get_latest_by = 'publish_date'"""

#-->8-managed: Django tomonidan ma'lumotlar bazasida ushbu model uchun jadval yaratish yoki o'zgartirish kerakligini belgilaydi. Default bo'yicha True.
"""class Meta:
    managed = False"""

#-->9-ordering: Model yozuvlarini default tartiblashni belgilaydi.
"""class Meta:
    ordering = ['name']"""

#-->10-permissions: Model uchun maxsus ruxsatlarni belgilaydi. Har bir ruxsat (permission) tuple ko'rinishida bo'ladi: (codename, verbose name).
"""class Meta:
    permissions = [
        ("can_publish", "Can Publish Posts"),
        ("can_edit", "Can Edit Posts"),
    ]"""

#-->11-unique_together: Bir nechta maydonlarning yagona kombinatsiyasini belgilaydi. Django 2.2 va undan keyingi versiyalarda bu parametr o'rniga UniqueConstraint foydalanish tavsiya etiladi.
"""class Meta:
    unique_together = ['name', 'date']"""

#-->12-index_together: Bir nechta maydonlarga indeks yaratadi. Django 2.2 va undan keyingi versiyalarda bu parametr o'rniga Index foydalanish tavsiya etiladi.
"""class Meta:
    index_together = ['name', 'date']"""

#-->13-constraints: Model uchun maxsus cheklovlarni belgilaydi. Bu Django 2.2 versiyasidan boshlab kiritilgan.
"""from django.db.models import UniqueConstraint, Q

class Meta:
    constraints = [
        UniqueConstraint(fields=['name', 'date'], name='unique_name_date'),
        UniqueConstraint(fields=['age'], condition=Q(age__gte=18), name='unique_adult_age')
    ]"""

#-->14-indexes: Model uchun indekslarni belgilaydi. Bu Django 2.2 versiyasidan boshlab kiritilgan.
"""from django.db import models

class Meta:
    indexes = [
        models.Index(fields=['name', 'date']),
        models.Index(fields=['age'], name='age_idx'),
    ]"""

#-------------------------------------------------------------------------------------
#Asosiy save() metodini chaqirish:
#Django modelida save() metodini chaqirganda, Django ma'lumotlar bazasida mos yozuvni saqlaydi.
"""from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

# Modeldan obyekt yaratish va saqlash
obj = MyModel(name='Javlonbek', age=25)
obj.save()"""

#save() metodini o'zgartirish:
#Agar siz saqlashdan oldin yoki keyin maxsus logika qo'shmoqchi bo'lsangiz, save() metodini #o'zgartirishingiz mumkin. Buning uchun metodni override qilishingiz kerak.
"""from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def save(self, *args, **kwargs):
        # Saqlashdan oldin qo'shimcha logika
        if self.age < 0:
            raise ValueError("Age cannot be negative")

        # Asosiy save() metodini chaqirish
        super(MyModel, self).save(*args, **kwargs)"""

#Qiyinchiliklarni saqlashdan oldin yoki keyin:
"""from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = 'Unnamed'
        super(MyModel, self).save(*args, **kwargs)"""