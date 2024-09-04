from django.urls import path
from . import views

urlpatterns = [
    path('objectives/', views.objective_list, name='objective_list'),
    path('objectives/create/', views.create_objective, name='create_objective'),
    path('activities/', views.activity_list, name='activity_list'),
    path('activities/create/', views.create_activity, name='create_activity'),
]
