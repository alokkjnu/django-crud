from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import StudentSerializers
from ..models import Student
from django.shortcuts import get_object_or_404


class StudentApiView(APIView):
    serializer_class = StudentSerializers

    def post(self, request):
        try:
            id = Student.objects.filter().last().id
            serializer = StudentSerializers(data=request.data)
            request.data['id'] = id + 1

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": e})

    def get(self, request, id=None):
        try:
            if id:
                student = get_object_or_404(Student, id=id)
                serializer = StudentSerializers(student)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                student = Student.objects.all()
                serializer = StudentSerializers(student, many=True)
                if serializer:
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": e})

    def put(self, request, id=None):
        try:
            student = get_object_or_404(Student, id=id)
            if student:
                serializer = StudentSerializers(student, partial=True, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"message": "Id not found!"})
        except ObjectDoesNotExist:
            return Response({"message": "Id not found!"})

    def delete(self, request, id):
        try:
            student = Student.objects.get(id=id)
            student.delete()
            return Response({"message": "data has been deleted"}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"message": "data not found"}, status=status.HTTP_404_NOT_FOUND)
