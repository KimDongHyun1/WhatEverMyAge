from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin 
from .models import CustomerUser

class CustomerUserAdmin(UserAdmin):    
    model = CustomerUser    
    list_display = ['email'] 

admin.site.register(CustomerUser, CustomerUserAdmin)