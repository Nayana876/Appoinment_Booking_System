
from django.contrib import admin
from register.models import UserProfileInfo, User,doctors

# admin.site.register(UserProfileInfo)
# admin.site.register(doctors)

@admin.register(doctors)
class doctorAdmin(admin.ModelAdmin):
    list_display = ('Name', 'address', 'phone','specialisation','email_address')
    ordering = ('Name',)
    
@admin.register(UserProfileInfo) 
class UserProfileInfoAdmin(admin.ModelAdmin):
    list_display=('Name','address','phone')   


