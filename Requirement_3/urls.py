from django.urls import path
from .views import InternsEnquiryFormView , InternsEnquiryFormUpdateDetailView
urlpatterns = [
    path('inquiryform/', InternsEnquiryFormView.as_view()),
    path('inquiryform/<int:id>/',InternsEnquiryFormUpdateDetailView.as_view()),
]
