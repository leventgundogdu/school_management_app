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
    # Add your logic for the admin page
    return render(request, 'admin/admin.html')

def student_page(request):
    # Add your logic for the student page
    return render(request, 'student/student.html')

def teacher_page(request):
    # Add your logic for the teacher page
    return render(request, 'teacher/teacher.html')

def grades(request):
    grades = Grade.objects.select_related('student').all()
    context = {'grades': grades}
    return render(request, 'admin/grades.html', context)

def edit_grade(request, grade_id):
    # Retrieve the grade object from the database
    try:
        grade = Grade.objects.get(id=grade_id)
    except Grade.DoesNotExist:
        return HttpResponse("Grade not found")

    if request.method == "POST":
        # Process the form data and update the grade
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect("grades")  # Replace "grades" with your actual URL name for the grades list page
    else:
        # Display the form for editing the grade
        form = GradeForm(instance=grade)

    # Render the template with the form
    context = {"form": form}
    return render(request, "admin/edit_grade.html", context)


def register_class(request):
    if request.method == 'POST':
        class_name = request.POST.get('class-name', '')
        teacher_id = request.POST.get('teacher', '')
        student_ids = request.POST.getlist('students')

        # Retrieve the teacher and students based on their IDs
        try:
            teacher = Teacher.objects.get(id=teacher_id)
        except Teacher.DoesNotExist:
            messages.error(request, 'Invalid teacher ID')
            return redirect('register-class')

        students = Student.objects.filter(id__in=student_ids)

        # Create a new class with the provided details
        new_class = Class(class_name=class_name, teacher=teacher)
        new_class.save()

        # Add the selected students to the class
        new_class.students.set(students)

        # Display a success message
        messages.success(request, 'Class Created!')

        # Redirect to the same page (register-class)
        return redirect('register-class')

    # Get all existing teachers and students
    teachers = Teacher.objects.all()
    students = Student.objects.all()
    classes = Class.objects.all()

    # Pass the teachers, students, and classes to the template
    context = {
        'teachers': teachers,
        'students': students,
        'classes': classes
    }

    return render(request, 'admin/register_class.html', context)



def create_user(request):
    if request.method == 'POST':
        # Check if teacher data is provided before saving
        teacher_firstname = request.POST.get('teacher-firstname', '')
        teacher_lastname = request.POST.get('teacher-lastname', '')
        teacher_id = request.POST.get('teacher-id', '')

        if teacher_firstname and teacher_lastname and teacher_id:
            teacher = Teacher(firstname=teacher_firstname, lastname=teacher_lastname, teacher_id=teacher_id)
            teacher.save()

        # Check if student data is provided before saving
        student_firstname = request.POST.get('student-firstname', '')
        student_lastname = request.POST.get('student-lastname', '')
        student_id = request.POST.get('student-id', '')

        if student_firstname and student_lastname and student_id:
            student = Student(firstname=student_firstname, lastname=student_lastname, student_id=student_id)
            student.save()

    # Get all existing teachers and students
    teachers = Teacher.objects.all()
    students = Student.objects.all()

    # Pass the teachers and students to the template
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
    print("Received student ID:", student_id)

    # Retrieve the student grades from the Grade table based on the student ID
    grades = Grade.objects.filter(student__student_id=student_id)
    context = {'grades': grades}
    return render(request, 'student/student_grades.html', context)




def teacher_login(request):
    return render(request, 'teacher/teacher.html')

def teacher_feed(request):
    return render(request, 'teacher/teacher_feed.html')

def edit_grades(request):
    # Process the form submission and save the grades
    if request.method == 'POST':
        # Retrieve and process the submitted grades
        # Save the grades to the database or perform any desired actions
        
        # Add a success message to be displayed after redirect
        messages.success(request, 'Grade submitted')
        
        # Redirect to the teacher feed page
        return redirect('teacher_feed')

    # Render the edit grades page with the form
    return render(request, 'teacher/edit_grades.html')
