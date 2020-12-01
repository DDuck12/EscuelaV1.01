from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from profesores.models import Profesor
from profesores.serializers import ProfesorSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def profesores(request):
    if request.method =='GET':
        profesores = Profesor.objects.all()
        serialized = ProfesorSerializer(profesores, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
    if request.method =='POST':
        profesor = ProfesorSerializer(data=request.data)
        if profesor.is_valid():
            profesor.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=profesor.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def profesor(request, profesor_id):
    profesor_obj = get_object_or_404(Profesor, id=profesor_id)

    if request.method =='GET':
        serialized = ProfesorSerializer(profesor_obj)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
    
    if request.method =='PUT':
        serialized = ProfesorSerializer(instance=profesor_obj, data=request.data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serialized.errors)

    if request.method =='DELETE':
        profesor_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)