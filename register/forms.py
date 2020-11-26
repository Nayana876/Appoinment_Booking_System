from django import forms
from register.models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    # name = forms.CharField(label='First Name', max_length=100)
    # lname = forms.CharField(label='Last Name', max_length=100)

    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
        
class UserProfileInfoForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput())
    # name = forms.CharField(label='First Name', max_length=100)
    class Meta():
        model = UserProfileInfo
        fields = ('Name','address','phone','age','profile_pic')