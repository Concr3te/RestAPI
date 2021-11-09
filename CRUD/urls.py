from django.urls import path
from . import views

urlpatterns = [
    path('', views.QuoteList, name ="quotes"),
    path('details/<str:pk>/', views.QuoteDetail, name = "detail"),
    path('create', views.QuoteCreate, name="create"),
    path('update/<str:pk>/', views.QuoteUpdate, name="update"),
    path('delete/<str:pk>/', views.QuoteDelete, name="delete"),
]
