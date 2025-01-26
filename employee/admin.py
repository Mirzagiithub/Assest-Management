from .models import MRole,Roleassign
# Register your models here.
from django.contrib import admin

class MRoleAdmin(admin.ModelAdmin):
    list_display=('id', 'role_name','status','created_at')
admin.site.register(MRole,MRoleAdmin),


class RoleassignAdmin(admin.ModelAdmin):
    list_display=('id', 'user','role','status','created_at')
admin.site.register(Roleassign,RoleassignAdmin),