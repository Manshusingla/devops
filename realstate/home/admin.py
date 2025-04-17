from django.contrib import admin
from .models  import Contact
from .models  import User_Accounts
from .models  import Properties

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','phone','message',)
@admin.register(User_Accounts)
class user_AccountAdmin(admin.ModelAdmin):
    list_display=('user_name','user_password','user_email','user_phone','user_address',)
@admin.register(Properties)
class PropertiesAdmin(admin.ModelAdmin):
    list_display=('property_name','property_pic','bedroom','washroom','square_feet','Property_location','Property_price','owner_name','contact_no')
    
