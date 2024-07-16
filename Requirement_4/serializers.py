from rest_framework import serializers
from .models import Technical_Assessment

class TechnicalAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technical_Assessment
        fields = '__all__'