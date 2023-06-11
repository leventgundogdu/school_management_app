"""school_management_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    
    path('admins/', views.admin_page, name='admin-page'),
    path('admins/register/', views.create_user, name='create-user'),
    path('admins/register-class/', views.register_class, name='register-class'),
    path('admins/grades/', views.grades, name='grades'),
    path('admins/edit-grade/<int:grade_id>/', views.edit_grade, name='edit-grade'),


    path('student/', views.student_login, name='student-login'),
    path('student/grades/<str:student_id>/', views.student_grades, name='student-grades'),
    
    path('teacher/', views.teacher_login, name='teacher-login'),
    path('teacher/feed/', views.teacher_feed, name='teacher-feed'),
    path('teacher/grades/edit/', views.edit_grades, name='edit-grades'),
    
]
