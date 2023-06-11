from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Teacher, Student, Class, Grade
from django.http import HttpResponse, HttpResponseRedirect
from .forms import GradeForm
import logging

logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'home.html')

def admin_page(request):
    return render(request, 'admin/admin.html')

def student_page(request):
    return render(request, 'student/student.html')

def teacher_page(request):
    return render(request, 'teacher/teacher.html')

def grades(request):
    grades = Grade.objects.select_related('student').all()
    context = {'grades': grades}
    return render(request, 'admin/grades.html', context)

def edit_grade(request, grade_id):
    try:
        grade = Grade.objects.get(id=grade_id)
    except Grade.DoesNotExist:
        return HttpResponse("Grade not found")

    if request.method == "POST":
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect("grades")
    else:
        form = GradeForm(instance=grade)

    context = {"form": form}
    return render(request, "admin/edit_grade.html", context)

def register_class(request):
    if request.method == 'POST':
        class_name = request.POST.get('class-name', '')
        teacher_id = request.POST.get('teacher', '')
        student_ids = request.POST.getlist('students')

        try:
            teacher = Teacher.objects.get(id=teacher_id)
        except Teacher.DoesNotExist:
            messages.error(request, 'Invalid teacher ID')
            return redirect('register-class')

        students = Student.objects.filter(id__in=student_ids)

        new_class = Class(class_name=class_name, teacher=teacher)
        new_class.save()

        new_class.students.set(students)

        messages.success(request, 'Class Created!')
        return redirect('register-class')

    teachers = Teacher.objects.all()
    students = Student.objects.all()
    classes = Class.objects.all()

    context = {
        'teachers': teachers,
        'students': students,
        'classes': classes
    }

    return render(request, 'admin/register_class.html', context)

def create_user(request):
    if request.method == 'POST':
        teacher_firstname = request.POST.get('teacher-firstname', '')
        teacher_lastname = request.POST.get('teacher-lastname', '')
        teacher_id = request.POST.get('teacher-id', '')

        if teacher_firstname and teacher_lastname and teacher_id:
            teacher = Teacher(firstname=teacher_firstname, lastname=teacher_lastname, teacher_id=teacher_id)
            teacher.save()

        student_firstname = request.POST.get('student-firstname', '')
        student_lastname = request.POST.get('student-lastname', '')
        student_id = request.POST.get('student-id', '')

        if student_firstname and student_lastname and student_id:
            student = Student(firstname=student_firstname, lastname=student_lastname, student_id=student_id)
            student.save()

    teachers = Teacher.objects.all()
    students = Student.objects.all()

    context = {
        'teachers': teachers,
        'students': students
    }

    return render(request, 'admin/registration.html', context)

def student_login(request):
    if request.method == 'POST':
        student_id = request.POST['student_id']
        return HttpResponseRedirect(f"/student/grades/{student_id}/")
    return render(request, 'student/student.html')

def student_grades(request, student_id):
    grades = Grade.objects.filter(student__student_id=student_id)
    context = {'grades': grades}
    return render(request, 'student/student_grades.html', context)

def teacher_login(request):
    if request.method == 'POST':
        teacher_id = request.POST['teacher_id']
        return redirect('teacher-feed', teacher_id=teacher_id)
    else:
        return render(request, 'teacher/teacher.html')

def teacher_feed(request):
    grades = Grade.objects.select_related('student').all()
    context = {'grades': grades}
    return render(request, 'teacher/teacher_feed.html', context)

def edit_grades(request, grade_id):
    try:
        grade = Grade.objects.get(id=grade_id)
    except Grade.DoesNotExist:
        return HttpResponse("Grade not found")

    if request.method == "POST":
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect("grades")
    else:
        form = GradeForm(instance=grade)

    context = {"form": form}
    return render(request, "teacher/edit_grades.html", context)
