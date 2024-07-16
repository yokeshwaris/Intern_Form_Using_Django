from django.db import models
from django.contrib.auth.models import User
class PersonalDetails(models.Model):
    # ID = models.AutoField(primary_key=True)
    First_Name = models.CharField(max_length = 40)
    Last_Name = models.CharField(max_length = 40)
    Referred_by = models.CharField(max_length = 40)
    DOB = models.DateField()
    Address = models.CharField(max_length = 60)
    Mobile_Number = models.CharField(max_length = 10)
    Email_ID = models.EmailField(unique = True)
    Qualification = models.CharField(max_length=40)
    Year_of_complementation = models.IntegerField()
    Created_by = models.CharField(max_length = 50 )
    Created_date_and_Time = models.DateTimeField(auto_now_add= True)
    Modified_by = models.CharField(max_length = 50 , default = 'Admin')
    Modified_date_and_Time = models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return self.ID