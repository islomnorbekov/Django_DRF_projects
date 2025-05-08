from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import (
    DrugUpdateView,
    DrugDeleteView,
)

urlpatterns = [
    path('', views.drug_list, name='drug_list'),
    path('edit/<int:pk>/', DrugUpdateView.as_view(), name='drug_edit'),
    path('delete/<int:pk>/', DrugDeleteView.as_view(), name='drug_delete'),
    path('add/', views.add_drug, name='add_drug'),
    path('signup/', views.signup_view, name='signup'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LoginView.as_view(), name='logout'),
]
