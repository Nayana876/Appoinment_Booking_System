
from django.db import models
from django.contrib.auth.models import User
from django import forms

# from django_select2.forms import Select2MultipleWidget
# from multiselectfield import MultiSelectField
# from django-weekday-field import weekday_field

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # Name = self.user.username
    Name = models.CharField("Name", max_length=100)
    address = models.CharField(max_length=300)
    phone = models.CharField("Phone no.", max_length=20, blank=True)
    age = models.CharField(max_length=3)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
   
def __str__(self):
  return self.user.username
# def 

class doctors(models.Model):
    d_id = models.AutoField(primary_key=True)
    Name = models.CharField("Name", max_length=100)
    address = models.CharField(max_length=300)
    phone = models.CharField("Phone no.", max_length=20, blank=True)
    email_address = models.EmailField("Email Address", blank=True) 
    department=(
      ('GENERALMEDICINE','GENERALMEDICINE'),
      ('PAEDIATRICS','PAEDIATRICS'),
      ('ONCOLOGY','ONCOLOGY'),
      ('CARDIOLOGIST','CARDIOLOGIST'),
      ('DERMATOLOGIST','DERMATOLOGIST'),
    )
  
    specialisation = models.CharField(
      max_length=20,choices=department,
      default='GENERALMEDICINE',
    )

    num_choices = ( ("1", "ONE"), ("2", "TWO"), ("3", "Three"), ("4", "Four"))
    day = models.CharField(max_length = 15, choices = num_choices)
    # addr=forms.MultipleChoiceField(choices=num_choices,widget=Select2MultipleWidget)
    # num_list = forms.MultipleChoiceField(choices=num_choices, required=True, widget=forms.CheckboxSelectMultiple(), label='Select No', initial=("1", "2"))
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    # weekdays = weekday_field.WeekdayField()

# def __str__(self):
#   return self.user.username