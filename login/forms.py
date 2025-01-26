from django import forms
from employee.models import MRole, Roleassign
from login.models import CustomUser
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import re
User = get_user_model()

class UserLoginForm(forms.Form):
    email_or_username = forms.CharField(label="Email or Username", max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)

CustomUser = get_user_model()
class EditCustomUserForm(forms.ModelForm):
  

    class Meta:
        model = CustomUser
        fields = [ 'first_name', 'last_name', 'email', 'is_active']
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise forms.ValidationError("First name is required.")
        if not first_name.isalpha():
            raise forms.ValidationError("First name can only contain alphabetic characters.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name:
            raise forms.ValidationError("Last name is required.")
        if not last_name.isalpha():
            raise forms.ValidationError("Last name can only contain alphabetic characters.")
        return last_name
   
    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = CustomUser.objects.filter(email=email).exclude(id=self.instance.id).first()
        
        if user:
            raise forms.ValidationError("Email is already taken.")
        return email
    
   

    
    
class CustomUserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}), 
        min_length=8,
        required=False,  # Password is optional for editing
        help_text="Leave empty if you don't want to change the password."
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}), 
        required=False,  # Password confirmation is optional for editing
        help_text="Leave empty if you don't want to change the password."
    )

    class Meta:
        model = CustomUser
        fields = [ 'first_name', 'last_name', 'email', 'is_active', 'password']
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise forms.ValidationError("First name is required.")
        if not first_name.isalpha():
            raise forms.ValidationError("First name can only contain alphabetic characters.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name:
            raise forms.ValidationError("Last name is required.")
        if not last_name.isalpha():
            raise forms.ValidationError("Last name can only contain alphabetic characters.")
        return last_name
   
    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = CustomUser.objects.filter(email=email).exclude(id=self.instance.id).first()
        
        if user:
            raise forms.ValidationError("Email is already taken.")
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is already taken.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password and len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        return password

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        
        if password and password != password_confirm:
            raise forms.ValidationError("The two password fields must match.")
        return password_confirm

    def save(self, commit=True):
        # Get the user instance from the form
        user = super().save(commit=False)
        
        # If a new password is provided, set the password
        password = self.cleaned_data.get('password')
        
        # If password is provided and not empty, hash and set it
        if password:
            user.set_password(password)  # Hash the new password
        # If no password is provided, we don't change the existing password.
        
        if commit:
            user.save()
        return user