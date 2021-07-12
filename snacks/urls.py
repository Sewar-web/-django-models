from django.urls import path
from .views import  SnackView ,SnackDetails

urlpatterns = [
    path('', SnackView.as_view(), name='snacks_list'),
    path('<int:pk>/', SnackDetails.as_view(), name='snacks_details'), 
]