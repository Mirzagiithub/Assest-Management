from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save, pre_save
from login.models import CustomUser

# Create your models here.

class MRole(models.Model):
    id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=255)
    status = models.CharField(max_length=1, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    updated_by = models.BigIntegerField(null=True,blank=True)
    class Meta:
        managed = True
        db_table = 'employee_mrole'
        verbose_name_plural = "MRole"

    def __str__(self):
        return self.role_name

class Roleassign(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    role = models.ForeignKey(MRole, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.BigIntegerField(null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'employee_roleassign'
        verbose_name_plural = "Roleassign"

    def __str__(self):
        return f"Roleassign {self.id}"