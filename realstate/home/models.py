from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    message=models.CharField(max_length=100)     
    def __str__(self):
        return self.first_name 
    
class User_Accounts(models.Model):
    user_name=models.CharField(max_length=100)
    user_password=models.CharField(max_length=100)
    user_email=models.CharField(max_length=100)
    user_phone=models.CharField(max_length=100)
    user_address=models.CharField(max_length=100)
    def __str__(self):
        return self.user_name
    

class Properties(models.Model):
        property_name=models.CharField(max_length=100)
        property_pic=models.FileField(upload_to="images/")
        bedroom=models.CharField(max_length=100)
        washroom=models.CharField(max_length=100)
        square_feet=models.CharField(max_length=100)
        Property_location=models.CharField(max_length=100)
        Property_price=models.CharField(max_length=100)
        owner_name=models.CharField(max_length=100)
        contact_no=models.CharField(max_length=100)    
        def __str__(self):
            return self.property_name        