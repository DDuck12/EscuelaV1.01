from django.urls import path

from clases.views import clase, clases

app_name = 'clases'
urlpatterns = [
    path('', clases),
    path('<int:clase_id>', clase),
]