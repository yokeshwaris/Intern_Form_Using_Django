from rest_framework.urls import path
from .views import UserView , LoginView




urlpatterns = [
    path('userregister/',UserView.as_view()),
    path('userlogin/',LoginView.as_view()),
]
