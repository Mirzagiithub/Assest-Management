from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import MRole, Roleassign
from login.models import CustomUser
from .forms import MRoleForm, RoleassignForm
from login.forms import CustomUserForm,EditCustomUserForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.http import Http404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control, never_cache
from django.views.decorators.csrf import csrf_exempt,csrf_protect,ensure_csrf_cookie,requires_csrf_token
from django.views.decorators.http import require_http_methods
# Define the CustomUser model using get_user_model
CustomUser = get_user_model()
################################################ User Management ################################################
# Add CustomUser view
@login_required
@require_http_methods(["GET", "POST"])
def add_custom_user(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"CustomUser {user.username} added successfully!")
            return redirect('user_list')  # Redirect to a page that lists users, for example
    else:
        form = CustomUserForm()
    
    return render(request, 'add_custom_user.html', {'form': form,'pages':pages})


# Edit CustomUser view
@login_required
@require_http_methods(["GET", "POST"])
def edit_custom_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)

    if request.method == 'POST':
        form = EditCustomUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()  # Save the form with or without a new password
            messages.success(request, f"User {user.username} updated successfully!")
            return redirect('user_list')  # Redirect to user detail view
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = EditCustomUserForm(instance=user)
        

    return render(request, 'edit_custom_user.html', {'form': form, 'user': user,'pages':pages})


# Enable CustomUser view
@login_required
def enable_custom_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    
    if user.is_active:
        messages.warning(request, f"CustomUser {user.username} is already enabled.")
    else:
        user.is_active = True
        user.save()
        messages.success(request, f"CustomUser {user.username} has been enabled.")
    
    return redirect('user_list')


# Disable CustomUser view
@login_required
def disable_custom_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    
    if not user.is_active:
        messages.warning(request, f"CustomUser {user.username} is already disabled.")
    else:
        user.is_active = False
        user.save()
        messages.success(request, f"CustomUser {user.username} has been disabled.")
    
    return redirect('user_list')


# Optional: User list view
@login_required
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'manage_user.html', {'users': users,'pages':pages})

################################################ End User Management ################################################

# View for adding a new role
def add_role(request):
    if request.method == 'POST':
        form = MRoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('role_list')  # Redirect to a page where all roles are listed
    else:
        form = MRoleForm()

    return render(request, 'add_role.html', {'form': form,'pages': pages})

def edit_role(request, id):
    role = get_object_or_404(MRole, id=id)
    
    if request.method == 'POST':
        form = MRoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return redirect('role_list')  # Redirect to the role list page after successful update
    else:
        form = MRoleForm(instance=role)
    
    return render(request, 'edit_role.html', {'form': form, 'role': role})

def role_list(request):
    roles = MRole.objects.all()
    return render(request, 'role_list.html', {'roles': roles,'pages': pages})


# View for assigning a role to a user
def assign_role(request):
    if request.method == 'POST':
        form = RoleassignForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('roleassign_list')  # Redirect to the list of role assignments
    else:
        form = RoleassignForm()

    return render(request, 'assign_role.html', {'form': form,'pages': pages})

def enable_roleassign(request, id):
    """Enable a role assignment by setting status to 'A'."""
    try:
        roleassign = get_object_or_404(Roleassign, id=id)
        roleassign.status = 'A'
        roleassign.save()
        messages.success(request, "Role Assign Enable Successfully.")
        return redirect('roleassign_list')
    except:
        messages.error(request, "Failed to Enable!.")
        return redirect('roleassign_list')
  


def disable_roleassign(request, id):
    """Disable a role assignment by setting status to 'I'."""
    try:
        roleassign = get_object_or_404(Roleassign, id=id)
        roleassign.status = 'I'
        roleassign.save()
        messages.success(request, "Role Assign Disable Successfully.")
        return redirect('roleassign_list')
    except:
        messages.error(request, "Failed to Disable!.")
        return redirect('roleassign_list')

# Optionally, you can add a list of roles and role assignments for management

def roleassign_list(request):
    roleassigns = Roleassign.objects.all()
    return render(request, 'roleassign_list.html', {'roleassigns': roleassigns,'pages': pages})