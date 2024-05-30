from django.contrib import admin
from .models import Employee, Tour, Reservation, TravelHistory, Payment

class TourAdmin(admin.ModelAdmin):
    list_display = ('id','Trip_Name','Trip_Type','Trip_Price','Trip_Capacity','Trip_Transportation','Trip_Accomadation','Created_Date','Trip_Employee','Trip_image','Trip_Detail')

    list_display_links = ('Trip_Name',)

    list_filter = ('Trip_Name','Trip_Type','Trip_Price','Trip_Capacity','Trip_Transportation','Trip_Accomadation','Created_Date','Trip_Employee','Trip_image','Trip_Detail')

    list_editable = ('Trip_Type','Trip_Price','Trip_Capacity','Trip_Transportation','Trip_Accomadation','Created_Date','Trip_Employee','Trip_image','Trip_Detail')
    

    list_per_page = 100

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id','Reservation_Time','Reservation_Price','Reservation_Note','Reservation_Confirmation','Reservation_Employee','Reservation_Trip','Reservation_Customer')
    list_display_links = ('id',)
    list_filter = ('Reservation_Time','Reservation_Price','Reservation_Confirmation','Reservation_Employee','Reservation_Trip')

    list_editable = ('Reservation_Confirmation',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','Employee_Name','Employee_Surname','Employee_Username','Employee_Password','Employee_Job','Employee_SuperID')

    list_filter = ('Employee_Name','Employee_Surname','Employee_Username','Employee_Password','Employee_Job','Employee_SuperID')

    list_display_links = ('id',)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id','Payment_Total','Payment_ReservationID')

    list_filter = ('Payment_Total','Payment_ReservationID')

    list_display_links = ('id',)
class TravelAdmin(admin.ModelAdmin):
    list_display = ('id','Travel_History_customer','Travel_History_Trip')

    list_filter = ('Travel_History_customer','Travel_History_Trip')

    list_display_links = ('id',)

admin.site.register(Tour,TourAdmin)
admin.site.register(Reservation,ReservationAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Payment,PaymentAdmin)
admin.site.register(TravelHistory,TravelAdmin)

