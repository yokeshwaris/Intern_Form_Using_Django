from rest_framework.urls import path
from .views import PersonalDetailCreateView , PersonalDetailUpdateDeleteView

urlpatterns = [
    path('personaldetails/',PersonalDetailCreateView.as_view()),
    path('personaldetails/<int:pk>/',PersonalDetailUpdateDeleteView.as_view()),

    
]
