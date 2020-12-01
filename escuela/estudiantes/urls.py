from django.urls import path

from estudiantes.views import estudiante, estudiantes

app_name = 'autores'
urlpatterns = [
    path('', estudiantes),
    path('<int:estudiante_id>', estudiante),
]