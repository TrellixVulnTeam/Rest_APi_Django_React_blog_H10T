from django.urls import path
from ..api import views

urlpatterns = [
    path('contact/', views.Contact_list),
    path('contact/<int:pk>/', views.ContactView),
]