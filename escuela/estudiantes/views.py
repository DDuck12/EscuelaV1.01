#from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
#from estudiantes.models import Estudiante

# Create your views here.
"""def get_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes/lista_estudiantes.html', {'estudiantes' : estudiantes})

def get_estudiante(request, estudiante_id):
    estudiante = Estudiante.objects.get(id=estudiante_id)
    return render(request, 'estudiantes/detalle.html', {'estudiante': estudiante})"""

from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from estudiantes.models import Estudiante
from estudiantes.serializers import EstudianteSerializer

@api_view(['GET', 'POST'])
def estudiantes(request):
    if request.method =='GET':
        estudiantes = Estudiante.objects.all()
        serialized = EstudianteSerializer(estudiantes, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
    if request.method =='POST':
        estudiante = EstudianteSerializer(data=request.data)
        if estudiante.is_valid():
            estudiante.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=estudiante.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def estudiante(request, estudiante_id):
    estudiante_obj = get_object_or_404(Estudiante, id=estudiante_id)

    if request.method =='GET':
        serialized = EstudianteSerializer(estudiante_obj)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
    
    if request.method =='PUT':
        serialized = EstudianteSerializer(instance=estudiante_obj, data=request.data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serialized.errors)
    
    if request.method =='DELETE':
        estudiante_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)