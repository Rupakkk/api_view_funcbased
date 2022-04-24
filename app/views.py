from functools import partial
import django
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status


# Create your views here.
@api_view(['GET','POST','PUT','PATCH','DELETE'])
# @csrf_exempt
def apiview(request,pk=None):
        if request.method == "GET":
            id = pk  # Remember this , pk comes directly
            if id is not None:
                data = Student.objects.get(id=id)
                serialize = StudentSerializer(data)
                return Response({'msg':'This is get Respons','serialize':serialize.data})
            else:
                data = Student.objects.all()
                serialize = StudentSerializer(data,many = True)
                return Response(serialize.data)
            
        if request.method == "POST":
            data = request.data  # This is parsed data
            print(data.get('address'))
            serialize = StudentSerializer(data=data)
            if serialize.is_valid():
                serialize.save()
                return Response({'msg':'This is post Respons'},status=status.HTTP_201_CREATED)
            else:
                return Response(serialize.errors)

        if request.method == "PUT":
            stu = Student.objects.get(id=pk)
            serialize = StudentSerializer(stu,data = request.data)
            if serialize.is_valid():
                serialize.save()
                return Response({'msg':'Complete Data edit complete'})
            else:
                return Response(serialize.errors)



        if request.method == "PATCH":
            stu = Student.objects.get(id=pk)
            serialize = StudentSerializer(stu,data = request.data,partial=True)
            if serialize.is_valid():
                serialize.save()
                return Response({'msg':'Partial Data edit complete'})
            else:
                return Response(serialize.errors)

        if request.method == "DELETE":
            if pk is not None:
                data = Student.objects.get(id=pk)
                data.delete()
                return Response({'msg':'Deletion Successful'},status=status.HTTP_508_LOOP_DETECTED)
            else:
                data = Student.objects.all()
                data.delete()
                return Response("DEletion Succesful")

            


