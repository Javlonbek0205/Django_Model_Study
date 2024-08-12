from django.contrib import admin
from .models import Project, Task, TeamMember
# Register your models here.
"""Django Admin Panelini Moslashtirish:

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
search_fields: first_name, last_name, email."""

class ProjectAdmin(admin.ModelAdmin):
  list_display = ['name', 'start_date', 'end_date']
  list_filter = ['start_date', 'end_date',]
  search_fields = ('name',)

class TaskAdmin(admin.ModelAdmin):
  list_display = ['title', 'project', 'due_date']
  list_filter = ['due_date', 'project',]
  search_fields = ('title',)

class TeamMemberAdmin(admin.ModelAdmin):
  list_display = ['first_name', 'last_name', 'email']
  search_fields = [ 'first_name', 'last_name', 'email',]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(TeamMember, TeamMemberAdmin )