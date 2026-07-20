from django.urls import path
from .views import *

urlpatterns = [
    path('students/',global_management),
    path('students/<pk>',specified_management)
]

