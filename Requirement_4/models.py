from django.db import models
class Technical_Assessment(models.Model):
 options=(
        (0,0),
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
    )
 
 Interns_Name = models.CharField(max_length=50)
 Domain = models.CharField(max_length=50)
 Date = models.DateField(auto_now_add = True)
 Assessed_By = models.CharField(max_length=50)
 Conceptual_Understanding = models.IntegerField(choices = options,default = 0)
 Understanding_and_explaining_Code = models.IntegerField(choices = options,default = 0)
 Technical_Skills = models.IntegerField(choices = options,default = 0)
 Analytical_Skills = models.IntegerField(choices = options,default = 0)
 Communication = models.IntegerField(choices = options,default = 0)
 Recommendations = models.TextField()
 Created_by = models.CharField(max_length = 50)
 Created_date_and_Time = models.DateTimeField(auto_now_add= True)
 Modified_by = models.CharField(max_length = 50 , default = 'Admin')
 Modified_date_and_Time = models.DateTimeField(auto_now_add= True)
 def __str__(self):
    return self.Interns_Name
 
