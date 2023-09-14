
from django.urls import path
from ..api.views import StudentApiView

urlpatterns = [
    path('student/', StudentApiView.as_view()),
    path('student/<int:id>', StudentApiView.as_view()),
]
