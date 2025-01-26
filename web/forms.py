from django import forms
from django.db.models import fields
from django.db.models.fields import CharField
from django.core import validators
from django.core.exceptions import ValidationError
import django.forms.utils
import django.forms.widgets
from django.core.validators import RegexValidator
from django.core import validators
from django.contrib.auth.password_validation import validate_password
import re
from django.forms.widgets import DateInput
from django.core.validators import EmailValidator
from django.contrib.auth.password_validation import validate_password
from .models import AssetGroupBase, AEEGrp, ETGGrp, ICTSGrp, SSAGrp,QAPMCGrp,ExcelFile,ASPGGrp




    
class AssetGroupForm(forms.ModelForm):
    class Meta:
        model = AssetGroupBase
        fields = [ 'asset_type', 'asset_name', 'asset_identifier', 'owner', 'custodian', 'user', 'asset_group', 'asset_location', 'security_classification', 'amc_warranty_end_date', 'backup_location', 'status']

    def clean_sl_no(self):
        sl_no = self.cleaned_data.get('sl_no')
        if sl_no == '':
            return None  # Handle empty strings and return None
        return sl_no


class AEEGrpForm(forms.ModelForm):
    class Meta:
        model = AEEGrp
        fields = '__all__'
    
    def clean_file(self):
        file = self.cleaned_data.get('file')
        if not file.name.endswith(('.xls', '.xlsx')):
            raise ValidationError("Only Excel files are allowed!")
        return file

class AspgGrpForm(forms.ModelForm):
    class Meta:
        model = ASPGGrp
        fields = '__all__'
    
    def clean_file(self):
        file = self.cleaned_data.get('file')
        if not file.name.endswith(('.xls', '.xlsx')):
            raise ValidationError("Only Excel files are allowed!")
        return file

class ETGGrpForm(forms.ModelForm):
    class Meta:
        model = ETGGrp
        fields = '__all__'
    
    def clean_file(self):
        file = self.cleaned_data.get('file')
        if not file.name.endswith(('.xls', '.xlsx')):
            raise ValidationError("Only Excel files are allowed!")
        return file

class ICTSGrpForm(forms.ModelForm):
    class Meta:
        model = ICTSGrp
        fields = '__all__'

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if not file.name.endswith(('.xls', '.xlsx')):
            raise ValidationError("Only Excel files are allowed!")
        return file

class SSAGrpForm(forms.ModelForm):
    class Meta:
        model = SSAGrp
        fields = '__all__'

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if not file.name.endswith(('.xls', '.xlsx')):
            raise ValidationError("Only Excel files are allowed!")
        return file

    
class QapmcGrpForm(forms.ModelForm):
    class Meta:
        model = QAPMCGrp
        fields = '__all__'

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if not file.name.endswith(('.xls', '.xlsx')):
            raise ValidationError("Only Excel files are allowed!")
        return file

class ExcelFileForm(forms.Form):
    file = forms.FileField(required=True)
    group = forms.ChoiceField(
        choices=[
            ('ICTSGrp', 'ICTS Group'),
            ('AEEGrp', 'AEE Group'),
            ('ASPGGrp', 'ASPG Group'),
            ('ETGGrp', 'ETG Group'),
            ('SSAGrp', 'SSA Group'),
            ('QAPMCGrp', 'QAPMC Group'),
        ],
        required=True
    )