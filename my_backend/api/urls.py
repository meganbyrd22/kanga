from django.urls import path
from . import views

urlpatterns = [
    path('recipe1/', views.recipe1, name='recipe1'),
    path('recipe2/', views.recipe2, name='recipe2'),
]
