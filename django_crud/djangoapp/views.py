from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from .forms import *
from .models import *


# Create your views here.

class StudentView:
    def create_student(request):
        if request.method == "POST":
            student_form = StudentForm(request.POST)
            if student_form.is_valid():
                student_form.save()
                student = Student.objects.all()
                return render(request, 'student-list.html', {'student': student})
        else:
            student_form = StudentForm()
        student = Student.objects.all()
        return render(request, 'index.html', {'student_form': student_form, 'student': student})

    def student_list(request):
        student = Student.objects.all()
        return render(request, 'student-list.html', {'student': student})

    def student_update(request, id):
        try:
            student_id = Student.objects.get(id=id)
            student = Student.objects.all()
            student_form = StudentForm(instance=student_id)
            if request.method == "POST":
                student_form = StudentForm(request.POST, instance=student_id)
                if student_form.is_valid():
                    student_form.save()
            return render(request, 'index.html', {'student_form': student_form, 'student': student})
        except ObjectDoesNotExist as e:
            print(e)

    def student_delete(request, id):
        try:
            student = Student.objects.get(id=id)
            student.delete()
            student = Student.objects.all()
            return render(request, 'student-list.html', {'student': student})
        except ObjectDoesNotExist as e:
            print(e)
