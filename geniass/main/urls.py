from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='main'),
    path('create', views.create, name='create'),
    path('task/<int:id>/', views.task_id, name='task_id'),
    path('delete/<int:id>/', views.delete, name='delete'),

    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]