from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_all_tasks, name='list'),
    path('create/', views.create_task, name='create'),
    path('delete/<int:id>/', views.delete_task, name='delete'),
    path('update/<int:id>/', views.update_task, name='update'),
]