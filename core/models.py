from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)

class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    teacher_id = models.CharField(max_length=20)

class Class(models.Model):
    id = models.AutoField(primary_key=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField('Student')
    class_name = models.CharField(max_length=100)

class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_field = models.ForeignKey(Class, on_delete=models.CASCADE)
    midterm = models.DecimalField(max_digits=5, decimal_places=2)
    final = models.DecimalField(max_digits=5, decimal_places=2)
