from django import forms
from .models import Department, Programme, Student, Item

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['dept_name']

class ProgrammeForm(forms.ModelForm):
    class Meta:
        model = Programme
        fields = ['pgm_name', 'dept']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'reg_num', 'pgm', 'year_adm', 'gender', 'email', 'phone', 'dob','photo',]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'type', 'gender']
