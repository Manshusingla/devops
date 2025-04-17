from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Contact as cnts
from .models import User_Accounts
from .models import Properties
# from .forms import Contact


# Create your views here.
def home(request):
    properties=Properties.objects.all()
    if request.user.is_authenticated:
        return render(request,"index.html",{"properties":properties})
    else:
        return render(request,"index1.html",{"properties":properties})


def login(request):
    if request.method=="POST":
        user_name=request.POST.get("user_name")
        user_password=request.POST.get("user_password")
        user = authenticate(request,username=user_name , password=user_password)
        print("ki hopgfya")
        if user is not None:
            auth_login(request, user)
            return redirect("index")
        else:
            return render(request,"login.html")
    else:    
        return render(request,"login.html")
def index(request):
    return redirect("/home")

def about(request):
    if request.user.is_authenticated:
        return render(request,"about.html")
    else:    
        return render(request,"about1.html")

def contact(request):
    if request.method=="POST":
            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            email=request.POST.get('email')
            address=request.POST.get('address')
            phone_number=request.POST.get('phone_number')
            message=request.POST.get('message')
            subject=request.POST.get('subject')
            reg=cnts(first_name=first_name,last_name=last_name,email=email,phone=phone_number,    message=message,)
            reg.save()
            return redirect("contact") 
    else:       
        if request.user.is_authenticated:
            return render(request,"contact.html")
        else:       
            return render(request,"contact1.html")

def services(request):
    if request.user.is_authenticated:
        return render(request,"services.html")
    else:
        return render(request,"services1.html")


def company_certification(request):
    if request.user.is_authenticated:
        return render(request,"company_certification.html")
    else:
        return render(request,"company_certification1.html")

     
def sign_up(request):
        if request.method=="POST":
            user_name=request.POST.get("user_name")
            user_password=request.POST.get("user_password")
            user_phone=request.POST.get("user_phone")
            user_email=request.POST.get("user_email")
            user_address=request.POST.get("user_address")
            user_info=User_Accounts(user_name=user_name,user_password=user_password,    user_email=user_email,user_phone=user_phone,user_address=user_address)
            user_info.save()
            user = User.objects.create_user(user_name, user_email, user_password)
            user.save()
            return render(request,"login.html")
        else:
            return render(request,"sign_up.html")

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect("/")
    else:
        return redirect("/")
    
def add_property(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            property_name=request.POST.get("property_name")
            # property_pic=request.POST.get("property_pic")
            property_pic=request.FILES.get("property_pic")
            print(" this is typwe" ,type(property_pic))
            bedroom=request.POST.get("bedroom")
            washroom=request.POST.get("washroom")
            square_feet=request.POST.get("square_feet")
            Property_location=request.POST.get("Property_location")
            Property_price=request.POST.get("Property_price")
            owner_name=request.POST.get("owner_name")
            contact_no=request.POST.get("contact_no")
            property_list=Properties(property_name=property_name,property_pic=property_pic,bedroom=bedroom,washroom=washroom,square_feet=square_feet,Property_location=Property_location,Property_price=Property_price,owner_name=owner_name,contact_no=contact_no)
            property_list.save()
            return redirect("/home/")
        else:    
            return render(request,"add_property.html")    
    else:
        return redirect("/login")    