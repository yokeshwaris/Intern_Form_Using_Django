from rest_framework import generics
from .models import Technical_Assessment
from .serializers import TechnicalAssessmentSerializer
from rest_framework.permissions import IsAuthenticated

class ListCreateTechnicalAssessmentView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Technical_Assessment.objects.all()
    serializer_class = TechnicalAssessmentSerializer
class RetrieveUpdateDeleteTechnicalAssessmentview(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Technical_Assessment.objects.all()
    serializer_class = TechnicalAssessmentSerializer
