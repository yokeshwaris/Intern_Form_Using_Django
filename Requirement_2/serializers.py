from rest_framework import serializers
from .models import PersonalDetails

class PersonalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalDetails
        # fields =('First_Name','Last_Name','Referred_by','DOB','Address','Mobile_Number','Email_ID','Qualification','Year_of_complementation') 
        fields="__all__"
        ref_name = 'EmpGenericsEmployee'