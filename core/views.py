from django.shortcuts import render, redirect
from django.contrib import messages

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
    return render(request, 'admin/grades.html')

def edit_grade(request):
    return render(request, 'admin/edit_grade.html')

def register_class(request):
    if request.method == 'POST':
        # Handle form submission and class creation here
        # Access form data using request.POST dictionary

        # Redirect to a success page or perform other actions
        return redirect('class-created')

    # Render the registration template for GET requests
    return render(request, 'admin/register_class.html')

def create_user(request):
    if request.method == 'POST':
        # Process form submission
        firstname = request.POST.get('teacher-firstname', '')
        lastname = request.POST.get('teacher-lastname', '')
        teacher_id = request.POST.get('teacher-id', '')
        
        # Create Teacher object or perform necessary actions
        
        firstname = request.POST.get('student-firstname', '')
        lastname = request.POST.get('student-lastname', '')
        student_id = request.POST.get('student-id', '')
        
        # Create Student object or perform necessary actions
        
        # Redirect to a success page or back to the admin page
        return redirect('admin-page')
        
    return render(request, 'admin/registration.html')


def student_login(request):
    if request.method == 'POST':
        student_id = request.POST.get('student-id')
        # Perform any necessary validation or processing
        # Redirect to the student grades page with the student ID
        return redirect('student-grades', student_id=student_id)
    return render(request, 'student/student.html')

def student_grades(request, student_id):
    # Retrieve the student's grades using the provided student ID
    # Replace the static data with your logic to fetch student grades
    grades = [
        {'class': 'English', 'grade': 85},
        {'class': 'Mathematics', 'grade': 92},
        {'class': 'Science', 'grade': 78},
    ]
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
