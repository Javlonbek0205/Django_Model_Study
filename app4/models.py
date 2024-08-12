from django.db import models

# Create your models here.
"""1-Topshiriq: Loyihalarni Boshqarish Tizimi
Ma'lumotlar Modellarini Yaratish:

Project modeli:

name (CharField): Loyihaning nomi.
description (TextField): Loyihaning qisqacha tavsifi.
start_date (DateField): Loyihaning boshlanish sanasi.
end_date (DateField): Loyihaning tugash sanasi.
Meta sinfidan foydalanib ordering ni start_date bo‘yicha sozlang.
Task modeli:

title (CharField): Vazifaning nomi.
description (TextField): Vazifaning qisqacha tavsifi.
due_date (DateField): Vazifaning bajarilishi lozim bo'lgan sana.
project (ForeignKey): Vazifa qaysi loyihaga tegishli ekanini belgilash.
Custom Method: Agar due_date o‘tib ketgan bo‘lsa, vazifani bajarmaganlikni aniqlovchi is_overdue methodini yozing.
TeamMember modeli:

first_name (CharField): Jamoa a’zosining ismi.
last_name (CharField): Jamoa a’zosining familiyasi.
email (EmailField): Jamoa a’zosining email manzili.
assigned_tasks (ManyToManyField): Jamoa a’zosiga yuklatilgan vazifalar.
Meta sinfidan foydalanib ordering ni last_name va first_name bo‘yicha sozlang.
Custom Method: Jamoa a’zosining to‘liq ismini qaytaruvchi get_full_name methodini yozing.
Miqyoslash, Customization va Advanced ORM Queries:

Aggregation: Har bir loyiha uchun jami vazifalar sonini va bajarilgan/bajarilmagan vazifalar sonini annotate yordamida hisoblang.
ORM Queries: select_related va prefetch_related yordamida vazifalar va ularga tegishli loyiha hamda jamoa a'zolarini bir vaqtning o‘zida yuklang.
Custom Manager Method: Task modeli uchun overdue_tasks methodini yarating, u qaysi vazifalar belgilangan muddatdan kechikkanini qaytarsin.
Django Admin Panelini Moslashtirish:

ProjectAdmin klassini yarating va list_display, list_filter, search_fields ni sozlang:

list_display: name, start_date, end_date.
list_filter: start_date, end_date.
search_fields: name.
TaskAdmin klassini yarating va list_display, list_filter, search_fields ni sozlang:

list_display: title, project, due_date.
list_filter: due_date, project.
search_fields: title.
TeamMemberAdmin klassini yarating va list_display, search_fields ni sozlang:

list_display: first_name, last_name, email.
search_fields: first_name, last_name, email.
Migrationlar:

Barcha modellaringiz uchun makemigrations va migrate buyruqlarini ishlating."""
import datetime
from django.db.models import Count
class Project(models.Model):
  name = models.CharField(max_length=120)
  description = models.TextField()
  start_date = models.DateField()
  end_date = models.DateField()
  class Meta:
    ordering = ['start_date']

class TaskManager(models.Manager):
  def overdue_tasks(self):
    today = datetime.date.today()
    return self.filter(due_date__lt = today)

class Task(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  due_date = models.DateField()
  project = models.ForeignKey(Project, on_delete=models.CASCADE)

  objects = TaskManager()

  def is_overdue(self):
    today = datetime.date.today()
    return today > self.due_date


class TeamMember(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.EmailField()
  assigned_tasks = models.ManyToManyField(Task)
  class Meta:
    ordering = ['last_name', 'first_name']

  def get_full_name(self):
    return f"{self.first_name} {self.last_name}"

#from django.db.models import Count, Case, When, IntegerField

"""projects_with_task_counts = Project.objects.annotate(
    total_tasks=Count('task'),
    completed_tasks=Count(
        Case(
            When(task__due_date__lt=datetime.date.today(), then=1),
            output_field=IntegerField(),
        )
    ),
    incomplete_tasks=Count(
        Case(
            When(task__due_date__gte=datetime.date.today(), then=1),
            output_field=IntegerField(),
        )
    )
)"""

"""tasks_with_project_and_teammembers = Task.objects.select_related('project').prefetch_related('teammember_set')
"""