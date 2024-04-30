from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone

# #helper function because django could not serial timezone direct so we return only 
# #date part of timezone
# #models.datefield(defailt=timezone.now) it was throwing error
# def get_current_date():
#     return timezone.now().date()


# # Create your models here.
# class Equipment(models.Model):
#     deviceName = models.CharField(max_length=50)
#     deviceType = models.CharField(max_length=25)
#     serialNum = models.CharField(max_length=30,unique=True)
#     cpu = models.CharField(max_length=30)
#     gpu = models.CharField(max_length=30)
#     assigned_to = models.ForeignKey(User,on_delete=models.CASCADE)
    
#     def __str__(self) -> str:
#         return self.deviceName
    
# class Reservation(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     date = models.DateField(default=get_current_date)
#     equipmentId = models.ForeignKey(Equipment,on_delete=models.CASCADE)
    
#     def __str__(self):
#         return f"{self.user.username} - {self.equipmentId.deviceName} on {self.date}"