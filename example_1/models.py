from django.db import models

# Create your models here.
"""1. Django Model Tushunchasi
Topshiriq 1: Event Model
•	Yaratish:
o	Event modelini yarating. Fieldlar:
	title: CharField, maksimal uzunlik 200 belgidan ko'p bo'lmasin.
	location: CharField, maksimal uzunlik 300 belgidan ko'p bo'lmasin.
	event_date: DateTimeField.
o	identifier nomli custom method qo'shing, bu metod har bir event uchun noyob identifikator yaratishi kerak.
•	Amalga oshirish:
o	Modelni admin.py faylida admin panelga qo'shing va title bo'yicha qidiruvni qo'shing.
Topshiriq 2: Person Model
•	Yaratish:
o	Person modelini yarating. Fieldlar:
	first_name: CharField, maksimal uzunlik 100 belgidan ko'p bo'lmasin.
	last_name: CharField, maksimal uzunlik 100 belgidan ko'p bo'lmasin.
	birthdate: DateField.
	email: EmailField.
o	full_name nomli custom method qo'shing, bu metod first_name va last_name ni birlashtirib qaytarishi kerak.
•	Amalga oshirish:
o	Modelni admin.py faylida admin panelga qo'shing va first_name, last_name bo'yicha qidiruvni qo'shing.
Topshiriq 3: Article Model
•	Yaratish:
o	Article modelini yarating. Fieldlar:
	title: CharField, maksimal uzunlik 200 belgidan ko'p bo'lmasin.
	content: TextField.
	published_at: DateTimeField.
o	was_published_recently nomli custom method qo'shing, bu metod maqolaning so'nggi 7 kun ichida nashr qilinganligini tekshirishi kerak.
•	Amalga oshirish:
o	Modelni admin.py faylida admin panelga qo'shing va published_at bo'yicha qidiruvni qo'shing.
Topshiriq 4: Customer Model
•	Yaratish:
o	Customer modelini yarating. Fieldlar:
	first_name: CharField, maksimal uzunlik 100 belgidan ko'p bo'lmasin.
	last_name: CharField, maksimal uzunlik 100 belgidan ko'p bo'lmasin.
	email: EmailField.
	created_at: DateTimeField, auto_now_add=True.
•	Amalga oshirish:
o	Modelni admin.py faylida admin panelga qo'shing va created_at bo'yicha qidiruvni qo'shing.
"""