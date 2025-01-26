from django import forms
from .models import MRole, Roleassign
from login.models import CustomUser
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.core.validators import validate_email
####################### User Form #######################################################



# Form for creating a new role
class MRoleForm(forms.ModelForm):
    class Meta:
        model = MRole
        fields = ['role_name', 'status']
        widgets = {
            'status': forms.Select(choices=[('A', 'Active'), ('I', 'Inactive')]),
        }

# Form for assigning a role to a user
class RoleassignForm(forms.ModelForm):
    class Meta:
        model = Roleassign
        fields = ['user', 'role', 'status']
        widgets = {
            'status': forms.Select(choices=[('A', 'Active'), ('I', 'Inactive')]),
        }

    # Custom validation for role assignment
    def clean(self):
        cleaned_data = super().clean()
        user = cleaned_data.get('user')
        role = cleaned_data.get('role')

        # Prevent assigning the same role to the user more than once
        if Roleassign.objects.filter(user=user, role=role).exists():
            raise forms.ValidationError("This role is already assigned to the user.")
        return cleaned_data

    # Customizing the user field to display first_name + last_name
    user = forms.ModelChoiceField(
        queryset=CustomUser.objects.all(),
        label="User",
        to_field_name='username',
        widget=forms.Select,
        empty_label="Select User"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Update the user field label to show first_name + last_name
        self.fields['user'].queryset = CustomUser.objects.all()
        self.fields['user'].label_from_instance = lambda obj: f"{obj.first_name} {obj.last_name}"