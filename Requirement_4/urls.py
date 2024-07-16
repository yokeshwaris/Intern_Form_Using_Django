from django.urls import path
from .views import ListCreateTechnicalAssessmentView , RetrieveUpdateDeleteTechnicalAssessmentview

urlpatterns = [
    path('technical/',ListCreateTechnicalAssessmentView.as_view()),
    path('technical/<int:pk>/',RetrieveUpdateDeleteTechnicalAssessmentview.as_view())
]
