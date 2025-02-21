from django.db import models
from django.contrib.auth.models import User

class Employees(models.Model):
    user = models.OneToOneField(User,
on_delete=models.CASCADE)
    role =models.CharField(max_length = 20,
choices=[('Admin','Admin') ,('Employee','Employee')])                        
 
 
 
class  LeaveRequest(models.Model):
    LEAVE_TYPES = [('sick_leave','Sick Leave'),('casual_leave','Casual Leave'),('paid_leave','Paid_Leave')]
    STATUS_CHOICES = [('pending','Pending'),('approved','Approved'),('rejected,"Rejected')]
    
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE) 
    leave_type = models.CharField(max_length= 20,choices=LEAVE_TYPES)
    start_date = models.DateField() 
    end_date =  models.DateField() 
    status = models.CharField(max_length= 10,choices =  STATUS_CHOICES,default = 'pending')
                      
                                
                                
                                
