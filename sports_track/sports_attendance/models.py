from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=255)
    
def __str__(self):
        return self.dept_name
    

class Programme(models.Model):
    pgm_id = models.AutoField(primary_key=True)
    pgm_name = models.CharField(max_length=255)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.pgm_name

class Student(models.Model):
    stud_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    reg_num = models.CharField(max_length=255,unique=True)
    pgm = models.ForeignKey(Programme, on_delete=models.CASCADE)
    year_adm = models.IntegerField()
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    photo = models.ImageField(upload_to='sports_attendance/student_photos/', null=True, blank=True)
    
    def __str__(self):
        return self.name

"""class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default="Unknown")  # Ensure default is set
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=20)
    role = models.CharField(max_length=255)
    
class Tutor(models.Model):
    tutor_id = models.AutoField(primary_key=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    pgm = models.ForeignKey(Programme, on_delete=models.CASCADE)"""

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=255)
    TYPE_CHOICES = [
        ('Individual', 'Individual'),
        ('Group', 'Group'),
        
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

"""class StudentItem(models.Model):
    stud = models.ForeignKey(Student, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    year = models.IntegerField()
    class Meta:
        unique_together = ('stud', 'item')"""





