from django.contrib import admin
from django.contrib.auth.models import User
from .models import Customer_Info
# Register your models here.





class CostumerAdmin(admin.ModelAdmin):
    list_display = ('id','Tel_No','Emergency_Number','Birthday','Gender')

    list_filter = ('Tel_No','Birthday','Gender')

    list_editable = ('Tel_No','Emergency_Number','Birthday','Gender')

    list_display_links = ('id',)


admin.site.register(Customer_Info,CostumerAdmin)