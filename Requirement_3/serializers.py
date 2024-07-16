from rest_framework import serializers
from .models import InternsEnguiryForm
class InternsEnquiryFormSerializers(serializers.ModelSerializer):
    class Meta:
        model = InternsEnguiryForm
        fields = ('Name',
                  'DOB',
                  'Marital_Status',
                  'Father_Name',
                  'Father_Occupation',
                  'Mother_Name',
                  'Mother_Occupation',
                  'Language_Known',
                  'Extra_Curricular_Activities',
                  'Email_ID',
                  'Mobile_Number',
                  'Permanent_Address',
                  'Current_Address',
                  'Qualification_With_Department',
                  'Year_of_PassedOut',
                  'Technical_Certifications',
                  'Reason_for_interest',
                  'internship_experience',
                  'Declaration',
                  
                  )
        