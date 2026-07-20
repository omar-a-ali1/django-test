from django.core.serializers import serialize
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from  .serializer import *

@api_view(['GET','POST'])
def global_management(request):
    if request.method == 'POST':
        serializer= StudentSerializer(request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    if request.method == 'GET':
        users = Student.objects.all()
        serializer = StudentSerializer(users,many=True)
        return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def specified_management(request,pk):
    try  :
        student = Student.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND);
        
    if request.method =='GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method =='DELETE':
        student.delete()
        Response('user deleted succfully')

        
