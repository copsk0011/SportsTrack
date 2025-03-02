from django.contrib import admin
from .models import Department, Programme, Student, Item

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dept_id', 'dept_name')
    search_fields = ('dept_name',)

@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ('pgm_id', 'pgm_name', 'dept')
    list_filter = ('dept',)
    search_fields = ('pgm_name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('stud_id', 'name', 'reg_num', 'pgm', 'year_adm', 'gender', 'email', 'phone', 'dob')
    list_filter = ('pgm', 'year_adm', 'gender')
    search_fields = ('name', 'reg_num', 'email')
    ordering = ('-year_adm',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'item_name', 'type', 'gender')
    search_fields = ('item_name',)
    list_filter = ('type', 'gender')