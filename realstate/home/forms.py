from django import forms
from .models import Properties

class Contact(forms.Form):
    first_name=forms.CharField(max_length=100,label="first name")
    last_name=forms.CharField(max_length=100,label="last name")
    email=forms.CharField(max_length=100,label="your email")
    phone=forms.IntegerField(label="your phone")
    message=forms.CharField(max_length=100,label="Message")


class Imageform(forms.ModelForm):
    class Meta:
        model=Properties
        fields='__all__'
        label={'photo':""}