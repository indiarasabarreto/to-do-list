from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_all_tasks, name='list'),
    path('create/', views.create_task, name='create'),
    path('delete/<int:id>/', views.delete_task, name='delete'),
    path('update/<int:id>/', views.update_task, name='update'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
]