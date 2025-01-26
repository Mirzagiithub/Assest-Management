from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import ManageICTSListView,ManageSSAListView,ManageAEECreateView,ManageAEEListView,ManageAEEUpdateView,ManageICTSCreateView,ManageICTSUpdateView,ManageQAPMCGrpCreateView,ManageQAPMCGrpListView,ManageQAPMCGrpUpdateView,ManageSSACreateView,ManageSSAUpdateView,ManageSTGCreateView,ManageSTGListView,ManageSTGUpdateView,ManageAspgCreateView,ManageAspgListView,ManageAspgUpdateView
from .views import ToggleICTSStatusView,ToggleAEEStatusView,ToggleAspgStatusView,ToggleQAPMCGrpStatusView,ToggleSSAStatusView,ToggleSTGStatusView,ManageAdminListView,ManageFinanceListView
urlpatterns = [

    # ICTSGrp URLs
     path('manage_admin',ManageAdminListView.as_view(), name='manage_admin'),
      path('manage_finance',ManageFinanceListView.as_view(), name='manage_finance'),
    
    path('manage_icts',ManageICTSListView.as_view(), name='manage_icts'),
    path('create_icts/',ManageICTSCreateView.as_view(), name='create_icts'),
    path('manage/icts/update/<int:pk>/',ManageICTSUpdateView.as_view(), name='update_icts'),
    path('manage/icts/toggle-status/<int:asset_id>/',ToggleICTSStatusView.as_view(), name='toggle_icts_status'),

    # AEEGrp URLs
    path('manage_aee/',ManageAEEListView.as_view(), name='manage_aee'),
    path('manage/aee/create/', ManageAEECreateView.as_view(), name='create_aee'),
    path('manage/aee/update/<int:pk>/', ManageAEEUpdateView.as_view(), name='update_aee'),
    path('manage/aee/toggle-status/<int:asset_id>/', ToggleAEEStatusView.as_view(), name='toggle_aee_status'),

    # AppliedAIGrp URLs
    path('manage_aspg/', ManageAspgListView.as_view(), name='manage_aspg'),
    path('manage/aspg/create/', ManageAspgCreateView.as_view(), name='create_aspg'),
    path('manage/aspg/update/<int:pk>/',ManageAspgUpdateView.as_view(), name='update_aspg'),
    path('manage/aspg/toggle-status/<int:asset_id>/', ToggleAspgStatusView.as_view(), name='toggle_aspg_status'),

    # STGGrp URLs
    path('manage_stg/', ManageSTGListView.as_view(), name='manage_stg'),
    path('manage/stg/create/',ManageSTGCreateView.as_view(), name='create_stg'),
    path('manage/stg/update/<int:pk>/', ManageSTGUpdateView.as_view(), name='update_stg'),
    path('manage/stg/toggle-status/<int:asset_id>/', ToggleSTGStatusView.as_view(), name='toggle_stg_status'),

    # SSAGrp URLs
    path('manage_ssa/', ManageSSAListView.as_view(), name='manage_ssa'),
    path('manage/ssa/create/',ManageSSACreateView.as_view(), name='create_ssa'),
    path('manage/ssa/update/<int:pk>/', ManageSSAUpdateView.as_view(), name='update_ssa'),
    path('manage/ssa/toggle-status/<int:asset_id>/', ToggleSSAStatusView.as_view(), name='toggle_ssa_status'),

   

    # QAPMCGrp URLs
    path('manage_qapmc/',ManageQAPMCGrpListView.as_view(), name='manage_qapmc'),
    path('manage/qapmc/create/', ManageQAPMCGrpCreateView.as_view(), name='create_qapmc'),
    path('manage/qapmc/update/<int:pk>/', ManageQAPMCGrpUpdateView.as_view(), name='update_qapmc'),
    path('manage/qapmc/toggle-status/<int:asset_id>/', ToggleQAPMCGrpStatusView.as_view(), name='toggle_qapmc_status'),

    # File upload
    path('upload-file/', views.upload_file, name='upload_file'),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)