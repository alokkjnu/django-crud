from django.urls import path
from .views import StudentView

urlpatterns = [
    path('', StudentView.create_student,name='create_student'),
    path('student-list/', StudentView.student_list,name='student_list'),
    path('student-update/<int:id>', StudentView.student_update,name='student-update'),
    path('student-delete/<int:id>', StudentView.student_delete,name='student-delete'),
]
