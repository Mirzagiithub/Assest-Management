from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.
class UserModel(UserAdmin):
     list_display = ('username','first_name','last_name','email',)
  #   list_filter = ('username',)
  #   form = MyUserChangeForm
  #   fieldsets = UserAdmin.fieldsets + (('user_type', {'fields': ('roles',)}),)
 

admin.site.register(CustomUser, UserModel)