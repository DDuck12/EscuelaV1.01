#from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
#from clases.models import Clase


# Create your views here.
"""def get_clases(request):
    clases = Clase.objects.all()
    return render(request, 'clases/lista_clases.html', {'clases' : clases})

def get_clase(request, clase_id):
    clase = get_object_or_404(Clase, id=clase_id)
    return render(request, 'clases/detalle.html', {'clase': clase, 'estudiantes': clase.estudiantes.all()})"""

from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from clases.models import Clase
from clases.serializers import ClaseSerializer

@api_view(['GET', 'POST'])
def clases(request):
    if request.method =='GET':
        clases = Clase.objects.all()
        serialized = ClaseSerializer(clases, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
    if request.method =='POST':
        clase = ClaseSerializer(data=request.data)
        if clase.is_valid():
            clase.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=clase.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def clase(request, clase_id):
    clase_obj = get_object_or_404(Clase, id=clase_id)

    if request.method =='GET':
        serialized = ClaseSerializer(clase_obj)
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    if request.method =='PUT':
        serialized = ClaseSerializer(instance=clase_obj, data=request.data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serialized.errors)

    if request.method =='DELETE':
        clase_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

