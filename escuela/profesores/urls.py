from django.urls import path

from profesores.views import profesor, profesores

app_name = 'profesores'
urlpatterns = [
    path('', profesores),
    path('<int:profesor_id>', profesor),
]