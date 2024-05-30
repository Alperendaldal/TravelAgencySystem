from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Employee(models.Model):
    Employee_Name = models.CharField(max_length=50,verbose_name='Employee Name')
    Employee_Surname = models.CharField(max_length=50,verbose_name='Employee Surname')
    Employee_Username = models.CharField(max_length=30,verbose_name='User Name',null=False)
    Employee_Password = models.CharField(max_length=50,verbose_name='Password',null=False)
    Employee_Job = models.CharField(max_length=50,verbose_name='Job Desciption')
    Employee_SuperID = models.ForeignKey('self', on_delete= models.SET_NULL,null=True,blank=True, related_name='subordinates')



class Tour(models.Model):
    Trip_Name = models.CharField(max_length=100, verbose_name='Trip Name')
    Trip_Type = models.CharField(max_length=50,verbose_name='Trip Type')
    Trip_Price = models.DecimalField(max_digits=10,decimal_places=3, verbose_name='Price')
    Trip_Capacity = models.IntegerField(verbose_name='Capacity')
    Trip_Transportation = models.CharField(max_length=100,verbose_name='Transportation')
    Trip_Accomadation = models.CharField(max_length=50,verbose_name='Accomadation')
    Created_Date = models.DateTimeField(verbose_name='Trip Date')
    Trip_image = models.CharField(max_length=50,verbose_name='Trip İmage')
    Trip_Employee = models.ForeignKey(Employee, on_delete= models.SET_NULL, null=True)
    Trip_Detail = models.TextField(verbose_name='Tour descirption')

    def __str__(self):
        return self.Trip_Name
    
    def get_image_path(self):
        return '/image/'+ self.Trip_image
    
    def id(self):
        return self.id


class Reservation(models.Model):
    Reservation_Time = models.DateTimeField(auto_now_add=True,verbose_name='Reservation Date')
    Reservation_Price = models.DecimalField(max_digits = 8,decimal_places=2,verbose_name='Reservation Price')
    Reservation_Note = models.TextField(verbose_name='Note')
    Reservation_Confirmation = models.BooleanField(default=False)
    Reservation_Employee = models.ForeignKey(Employee, on_delete= models.SET_NULL,null=True)
    Reservation_Trip = models.ForeignKey(Tour, on_delete= models.SET_NULL,null=True)
    Reservation_Customer = models.ForeignKey(User, on_delete= models.SET_NULL,null=True)

    def id(self):
        return self.id


class TravelHistory(models.Model):
    Travel_History_customer = models.ForeignKey(User,on_delete= models.SET_NULL,null=True)
    Travel_History_Trip = models.ForeignKey(Tour, on_delete=models.SET_NULL,null=True)
    Travel_History_Reservation = models.ForeignKey(Reservation,on_delete=models.SET_NULL,null=True)
    Travel_History_Created_Date = models.DateTimeField(verbose_name='Record Date')

class Payment(models.Model):
    Payment_Total = models.DecimalField(max_digits = 10,decimal_places=3,verbose_name='Total Price')
    Payment_ReservationID = models.ForeignKey(Reservation,on_delete=models.SET_NULL,null=True)