from turtle import home
from django.urls import path
from .import views

urlpatterns=[
    path('',views.home),
    path('registrarCurso/',views.registrarCurso),
    path('eliminarCurso/<codigo>',views.eliminarCurso),
    path('obtenerCurso/<codigo>', views.obtenerCurso),
    path('editarCurso/<codigo>',views.editarCurso)
]