from django.db import models
class InternsEnguiryForm(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length = 40)
    DOB = models.DateField()
    Marital_Status = models.CharField(max_length = 20)
    Father_Name = models.CharField(max_length = 40)
    Father_Occupation = models.CharField(max_length = 40)
    Mother_Name = models.CharField(max_length = 40)
    Mother_Occupation = models.CharField(max_length = 40)
    Language_Known = models.CharField(max_length = 60)
    Extra_Curricular_Activities = models.CharField(max_length = 70)
    Email_ID = models.EmailField(unique = True)
    Mobile_Number = models.CharField(max_length = 12)
    Permanent_Address = models.CharField(max_length = 70)
    Current_Address = models.CharField(max_length = 70)
    Qualification_With_Department = models.CharField(max_length = 40)
    Year_of_PassedOut = models.IntegerField()
    Technical_Certifications = models.CharField(max_length = 40)
    Reason_for_interest = models.CharField(max_length = 40)
    internship_experience = models.CharField(max_length = 40)
    Declaration = models.CharField(max_length = 40)
    Created_by = models.CharField(max_length = 50)
    Created_date_and_Time = models.DateTimeField(auto_now_add=True)
    Modified_by = models.CharField(max_length = 50,default = True)
    Modified_date_and_Time = models.DateTimeField(auto_now_add=True)


    
    def __str__(self):
        return self.Name