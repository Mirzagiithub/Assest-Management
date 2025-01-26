from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from .forms import UserLoginForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control, never_cache
from django.views.decorators.csrf import csrf_exempt,csrf_protect,ensure_csrf_cookie,requires_csrf_token
from django.views.decorators.http import require_http_methods
import logging
from employee.models import Roleassign
# Create your views here.
# Set up logging
logger = logging.getLogger(__name__)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login_page(request):
    form =UserLoginForm()
    context ={
        'form':form,
    }
    return render(request,'login.html',context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login_view(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    
    form = UserLoginForm(request.POST)
    
    if form.is_valid():
        email_or_username = form.cleaned_data.get('email_or_username')
        password = form.cleaned_data.get('password')
        
        # Determine whether the input is an email or username
        if '@' in email_or_username:
            # It's an email, use custom EmailBackEnd
            user = authenticate(request, username=email_or_username, password=password, backend='path.to.EmailBackEnd')
        else:
            # It's a username, use Django's default authentication
            user = authenticate(request, username=email_or_username, password=password)  # This will use the default backend
        #print("User Login with username : ", user)
        if user is not None:
        #try:
            if user.is_superuser and user.is_active:
                login(request, user)
                return redirect('super_admin_dashboard')
            elif user is not None:
                    login(request, user)
                    is_active = user.is_active
                    type_obj = Roleassign.objects.get(user=user.id, status='T')
                    user_type =type_obj.role.id 
                    if user_type == 1 and user.is_active==True:        
                        return redirect('manage_icts')             
                    elif user_type == 2 and is_active==True:
                        return redirect('manage_ssa')          
                    elif user_type == 3 and is_active==True:
                        return redirect('manage_aee')         
                    elif user_type == 4 and is_active==True:
                        return redirect('manage_aspg')      
                    elif user_type == 5 and is_active==True:
                        return redirect('manage_stg')   
                    elif user_type == 6 and is_active==True:
                        return redirect('manage_qapmc')     
                    
                 
                    else:
                        messages.error(request, "Your Profile is not Registered, Please Contact Admin!")
                        return redirect('index')
    
            else:
                messages.error(request, "Invalid Login Credentials! or contact Administrator")
                return redirect('index')
            
       # except Exception as e:
        #    logger.error(f"Login error: {str(e)}")
        #    messages.error(request, "An unexpected error occurred. Please try again.")
       #     return redirect("login_page")
        else:
            messages.error(request, "Invalid email or password. Please try again.")
            return redirect("login_page")
    else:
        messages.error(request, "Invalid form submission.")
        return redirect('login_page')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def super_admin_dashboard(request):
    
    return render(request,'admin_dashboard.html')


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('login_page')