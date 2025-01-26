from django.db import models
from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import JSONField



class AssetGroupBase(models.Model):
    ASSET_TYPE_CHOICES = [
        ('Data / Information', 'Data / Information'),
        ('Infrastructure Systems (Hardware)', 'Infrastructure Systems (Hardware)'),
        ('Software / Applications', 'Software / Applications'),
        ('Support Systems', 'Support Systems'),
        ('Service', 'Service'),
        ('Human Resources', 'Human Resources'),
        ('Physical Media', 'Physical Media'),
        ('Facilities', 'Facilities'),
    ]

    SECURITY_CLASSIFICATION_CHOICES = [
        ('Confidential', 'Confidential'),
        ('Restricted', 'Restricted'),
        ('Public', 'Public'),
        ('Internal', 'Internal'),
    ]

    id = models.AutoField(primary_key=True,auto_created=True)
    asset_type = models.CharField(max_length=50, choices=ASSET_TYPE_CHOICES, verbose_name="Asset Type")
    asset_name = models.CharField(max_length=255, verbose_name="Asset Name")
    asset_identifier = models.CharField(max_length=255, verbose_name="Asset Identifier", unique=True)
    owner = models.CharField(max_length=255, verbose_name="Owner")
    group_name = models.CharField(max_length=255, verbose_name="Group Name", blank=True)
    custodian = models.CharField(max_length=255, verbose_name="Custodian")
    user = models.CharField(max_length=255, verbose_name="Assigned User")
    asset_type_description = models.TextField(verbose_name="Asset Type Description", blank=True)
    asset_group = models.CharField(max_length=255, verbose_name="Asset Group", blank=True)
    asset_location = models.CharField(max_length=255, verbose_name="Location", blank=True)
    security_classification = models.CharField(max_length=50, choices=SECURITY_CLASSIFICATION_CHOICES, verbose_name="Security Classification")
    amc_warranty_end_date = models.DateField(verbose_name="AMC/Warranty End Date", null=True, blank=True)
    backup_location = models.CharField(max_length=255, verbose_name="Backup Location", blank=True)
    status = models.CharField(max_length=1, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.asset_name} ({self.asset_identifier})"

class AEEGrp(AssetGroupBase):
    class Meta:
        db_table = 'aee_grp'
        verbose_name_plural = "AEE_info"

class ASPGGrp(AssetGroupBase):
    class Meta:
        db_table = 'aspg_grp'
        verbose_name_plural = "aspg_info"

class ETGGrp(AssetGroupBase):
    class Meta:
        db_table = 'etg_grp'
        verbose_name_plural = "ETG_info"

class ICTSGrp(AssetGroupBase):
    class Meta:
        db_table = 'icts_grp'
        verbose_name_plural = "ICTS_info"

class SSAGrp(AssetGroupBase):
    class Meta:
        db_table = 'ssa_grp'
        verbose_name_plural = "SSA_info"



class QAPMCGrp(AssetGroupBase):
    class Meta:
        db_table = 'qapmc_grp'
        verbose_name_plural = "qapmc_info"

class AdminGrp(AssetGroupBase):
    class Meta:
        db_table = 'admin_grp'
        verbose_name_plural = "admin_info"

class FinanceGrp(AssetGroupBase):
    class Meta:
        db_table = 'finanace_grp'
        verbose_name_plural = "finance_info"



###################
class ExcelFile(models.Model):
    GROUP_CHOICES = [
        ('ICTSGrp', 'ICTS'),
        ('AEEGrp', 'AEE'),
        ('ASPG', 'ASPG'),
        ('STGGrp', 'STG'),
        ('SSAGrp', 'SSA'),
        ('AdminGrp', 'Admin'),
        ('FinanceGrp', 'Finance'),
        ('QAPMCGrp', 'QAPMC'),
    ]
    group = models.CharField(max_length=50, choices=GROUP_CHOICES)
    file = models.FileField(upload_to='excel_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Excel file uploaded at {self.uploaded_at}"
    
    class Meta:
        managed = True
        db_table = 'excel_file'
        verbose_name_plural = "Excel Files"

# Model for storing the data of each row from the Excel file
class ExcelData(models.Model):
    excel_file = models.ForeignKey(ExcelFile, on_delete=models.CASCADE, related_name="data_entries")
    data = models.JSONField()  
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Data from {self.excel_file} uploaded at {self.uploaded_at}"
    
    class Meta:
        managed = True
        db_table = 'excel_data'
        verbose_name_plural = "Excel Data"