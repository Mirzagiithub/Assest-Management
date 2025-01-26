from django.contrib import admin

# Register your models here.
from .models import ICTSGrp,ExcelFile,ExcelData,SSAGrp, ETGGrp,QAPMCGrp,AEEGrp,ASPGGrp

class ICTSGrpAdmin(admin.ModelAdmin):
    list_display=('id', 'asset_type','asset_name','owner','group_name','custodian','user')
admin.site.register(ICTSGrp,ICTSGrpAdmin),

class ExcelFilepAdmin(admin.ModelAdmin):
    list_display=('id', 'group','file','uploaded_at')
admin.site.register(ExcelFile,ExcelFilepAdmin),

class ExcelDataAdmin(admin.ModelAdmin):
    list_display=('id', 'excel_file','data','uploaded_at')
admin.site.register(ExcelData,ExcelDataAdmin),

class SSAGrpAdmin(admin.ModelAdmin):
    list_display=('id', 'asset_type','asset_name','owner','group_name','custodian','user')
admin.site.register(SSAGrp,SSAGrpAdmin),

class QAPMCGrpGrpAdmin(admin.ModelAdmin):
    list_display=('id', 'asset_type','asset_name','owner','group_name','custodian','user')
admin.site.register(QAPMCGrp,QAPMCGrpGrpAdmin),

class AEEGrpAdmin(admin.ModelAdmin):
    list_display=('id', 'asset_type','asset_name','owner','group_name','custodian','user')
admin.site.register(AEEGrp,AEEGrpAdmin),

class STGGrpAdmin(admin.ModelAdmin):
    list_display=('id', 'asset_type','asset_name','owner','group_name','custodian','user')
admin.site.register(ETGGrp,STGGrpAdmin),

class ASPGGrpAdmin(admin.ModelAdmin):
    list_display=('id', 'asset_type','asset_name','owner','group_name','custodian','user')
admin.site.register(ASPGGrp,ASPGGrpAdmin),

