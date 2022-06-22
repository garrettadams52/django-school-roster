from django.shortcuts import render
from django.http import HttpResponse
from .models import School # import our School class

my_school = School("Django School") # create a school instance


def index(request):
    my_data = { 
        "school_name": my_school.name
    }
    return render(request, "pages/index.html", my_data)


def list_staff(request):
    my_data = { 
        "school_staff": my_school.staff
    }
    return render(request, "pages/staff.html", my_data)


def staff_detail(request, employee_id):
    staff_mem = my_school.find_staff_by_id(employee_id)
    my_data = {
        'staff_mem':staff_mem 
    }
    return render(request, "pages/staff_detail.html", my_data)


def list_students(request):
    my_data = { 
        "school_students": my_school.students
    }
    return render(request, "pages/students.html", my_data)



def student_detail(request, student_id):
    student = my_school.find_student_by_id(student_id)
    my_data = {
        'student' : student
    }
    return render(request, "pages/student_detail.html", my_data)