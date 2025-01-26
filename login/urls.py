from django.urls import path
from .views import login_page, login_view,super_admin_dashboard,logout_request

urlpatterns = [
    path('', login_page, name='login_page'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_request, name="logout"),
    path('super_admin_dashboard/', super_admin_dashboard, name='super_admin_dashboard'),
]