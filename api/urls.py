from django.urls import path
from .views import TaskListCreate, TaskDetail, PredictECG

urlpatterns = [
    path('tasks/', TaskListCreate.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('predict/', PredictECG.as_view(), name='predict-ecg'),
]