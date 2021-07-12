from django.urls import path
from .views import HomeView , SnackView ,SnackDetails

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  
    path('snacks/', SnackView.as_view(), name='snacks_list'),
    path('<int:pk>/', SnackDetails.as_view(), name='snacks_details'), 
]