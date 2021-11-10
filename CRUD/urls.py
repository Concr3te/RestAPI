from django.urls import path
from . import views
from .views import CustomAuthToken, QuotesView, QuoteDetail

urlpatterns = [
    path('', QuotesView.as_view(), name ="quotes"),
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('quote/<str:pk>/', views.QuoteDetail.as_view(), name = "detail"),
]
