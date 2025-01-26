from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.cache import cache_control
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
import pandas as pd
from .models import AEEGrp, ETGGrp, ICTSGrp, SSAGrp,QAPMCGrp,ASPGGrp,AdminGrp,FinanceGrp
from .forms import AEEGrpForm, ETGGrpForm, ICTSGrpForm, SSAGrpForm,QapmcGrpForm,ExcelFileForm ,AspgGrpForm
from django.contrib.auth.mixins import LoginRequiredMixin






############################################################################## ICTS Group ####################################################################################

class ManageICTSListView(LoginRequiredMixin,ListView):
    model = ICTSGrp
    template_name = 'manage_ictsgrp.html'
    context_object_name = 'icts_list'
    
    def get_queryset(self):
        queryset = ICTSGrp.objects.all()
        asset_identifier = self.request.GET.get('asset_identifier', None)
        if asset_identifier:
            queryset = queryset.filter(asset_identifier__icontains=asset_identifier)
        return queryset

class ManageICTSCreateView(LoginRequiredMixin,CreateView):
    model = ICTSGrp
    form_class = ICTSGrpForm  
    success_url = reverse_lazy('manage_icts')
    template_name = 'manage_ictsgrp.html'

class ManageICTSUpdateView(LoginRequiredMixin,UpdateView):
    model = ICTSGrp
    form_class = ICTSGrpForm
    template_name = 'manage_ictsgrp.html'
    success_url = reverse_lazy('manage_icts')

class ToggleICTSStatusView(LoginRequiredMixin,View):
    def post(self, request, *args, **kwargs):
        asset_id = kwargs.get('asset_id')
        asset = get_object_or_404(ICTSGrp, pk=asset_id)

        
        if asset.status == 'A':
            asset.status = 'I'
            messages.success(request, f"Asset '{asset.owner}' has been deactivated.")
        else:
            asset.status = 'A'
            messages.success(request, f"Asset '{asset.owner}' has been activated.")

        # Save the changes and redirect
        asset.save()
        return redirect('manage_icts')
    
##############################################################################################     AEEGrp Views:           ##############################################################################################
class ManageAEEListView(LoginRequiredMixin,ListView):
    model = AEEGrp
    template_name = 'manage_aeegrp.html'
    context_object_name = 'aee_list'
    def get_queryset(self):
        queryset = AEEGrp.objects.all()
        asset_identifier = self.request.GET.get('asset_identifier', None)
        if asset_identifier:
            queryset = queryset.filter(asset_identifier__icontains=asset_identifier)
        return queryset



class ManageAEECreateView(LoginRequiredMixin,CreateView):
    model = AEEGrp
    form_class = AEEGrpForm  
    template_name = 'manage_aeegrp.html'
    success_url = reverse_lazy('manage_aee')

class ManageAEEUpdateView(LoginRequiredMixin,UpdateView):
    model = AEEGrp
    form_class = AEEGrpForm
    template_name = 'manage_aeegrp.html'
    success_url = reverse_lazy('manage_aee')

class ToggleAEEStatusView(LoginRequiredMixin,View):
    def post(self, request, *args, **kwargs):
        asset_id = kwargs.get('asset_id')
        asset = get_object_or_404(AEEGrp, pk=asset_id)

        # Toggle the status
        if asset.status == 'A':
            asset.status = 'I'
            messages.success(request, f"Asset '{asset.owner}' has been deactivated.")
        else:
            asset.status = 'A'
            messages.success(request, f"Asset '{asset.owner}' has been activated.")

        # Save the changes and redirect
        asset.save()
        return redirect('manage_aee')


##############################################################################################    AEEGrp Views: END        ###########################################################################################
    


##############################################################################################   AppliedAIGrp Views         ###########################################################################################
class ManageAspgListView(LoginRequiredMixin,ListView):
    model = ASPGGrp
    template_name = 'manage_appliedaigrp.html'
    context_object_name = 'aspg_list'
    def get_queryset(self):
        queryset = ASPGGrp.objects.all()
        asset_identifier = self.request.GET.get('asset_identifier', None)
        if asset_identifier:
            queryset = queryset.filter(asset_identifier__icontains=asset_identifier)
        return queryset

class ManageAspgCreateView(LoginRequiredMixin,CreateView):
    model = ASPGGrp
    form_class = AspgGrpForm  # Make sure to create a form for this model
    template_name = 'manage_appliedaigrp.html'
    success_url = reverse_lazy('manage_aspg')
class ManageAspgUpdateView(LoginRequiredMixin,UpdateView):
    model = ASPGGrp
    form_class = AspgGrpForm
    template_name = 'manage_appliedaigrp.html'
    success_url = reverse_lazy('manage_aspg')

class ToggleAspgStatusView(LoginRequiredMixin,View):
    def post(self, request, *args, **kwargs):
        asset_id = kwargs.get('asset_id')
        asset = get_object_or_404(ASPGGrp, pk=asset_id)

        # Toggle the status
        if asset.status == 'A':
            asset.status = 'I'
            messages.success(request, f"Asset '{asset.asset_name}' (Owner: {asset.owner}) has been deactivated.")
        else:
            asset.status = 'A'
            messages.success(request, f"Asset '{asset.asset_name}' (Owner: {asset.owner}) has been activated.")

        # Save the changes and redirect
        asset.save()
        return redirect('manage_aspg')

##############################################################################################   AppliedAIGrp Views   END      ###########################################################################################

   
##############################################################################################      STGGrp Views          ##############################################################################################

class ManageSTGListView(LoginRequiredMixin,ListView):
    model = ETGGrp
    template_name = 'manage_stggrp.html'
    context_object_name = 'stg_list'

    def get_queryset(self):
        queryset = ETGGrp.objects.all()
        asset_identifier = self.request.GET.get('asset_identifier', None)
        if asset_identifier:
            queryset = queryset.filter(asset_identifier__icontains=asset_identifier)
        return queryset


class ManageSTGCreateView(LoginRequiredMixin,CreateView):
    model = ETGGrp
    form_class = ETGGrpForm  # Make sure to create a form for this model
    template_name = 'manage_stggrp.html'
    success_url = reverse_lazy('manage_stg')


class ManageSTGUpdateView(LoginRequiredMixin,UpdateView):
    model = ETGGrp
    form_class = ETGGrpForm
    template_name = 'manage_stggrp.html'
    success_url = reverse_lazy('manage_stg')


class ToggleSTGStatusView(LoginRequiredMixin,View):
    def post(self, request, *args, **kwargs):
        asset_id = kwargs.get('asset_id')
        asset = get_object_or_404(ETGGrp, pk=asset_id)

        # Toggle the status
        if asset.status == 'A':
            asset.status = 'I'
            messages.success(request, f"Asset '{asset.owner}' has been deactivated.")
        else:
            asset.status = 'A'
            messages.success(request, f"Asset '{asset.owner}' has been activated.")

        # Save the changes and redirect
        asset.save()
        return redirect('manage_stg')


##############################################################################################       STGGrp Views END        ###########################################################################################


   
##############################################################################################     SSAGrp Views           ##############################################################################################

class ManageSSAListView(LoginRequiredMixin,ListView):
    model = SSAGrp
    template_name = 'manage_ssagrp.html'
    context_object_name = 'ssa_list'

    def get_queryset(self):
        queryset = SSAGrp.objects.all()
        asset_identifier = self.request.GET.get('asset_identifier', None)
        if asset_identifier:
            queryset = queryset.filter(asset_identifier__icontains=asset_identifier)
        return queryset


class ManageSSACreateView(LoginRequiredMixin,CreateView):
    model = SSAGrp
    form_class = SSAGrpForm  # Make sure to create a form for this model
    template_name = 'manage_ssagrp.html'
    success_url = reverse_lazy('manage_ssa')


class ManageSSAUpdateView(LoginRequiredMixin,UpdateView):
    model = SSAGrp
    form_class = SSAGrpForm
    template_name = 'manage_ssagrp.html'
    success_url = reverse_lazy('manage_ssa')


class ToggleSSAStatusView(LoginRequiredMixin,View):
    def post(self, request, *args, **kwargs):
        asset_id = kwargs.get('asset_id')
        asset = get_object_or_404(SSAGrp, pk=asset_id)

        # Toggle the status
        if asset.status == 'A':
            asset.status = 'I'
            messages.success(request, f"Asset '{asset.owner}' has been deactivated.")
        else:
            asset.status = 'A'
            messages.success(request, f"Asset '{asset.owner}' has been activated.")

        # Save the changes and redirect
        asset.save()
        return redirect('manage_ssa')


##############################################################################################      SSAGrp Views END          ###########################################################################################


   
##############################################################################################        AdminGrp Views        ##############################################################################################


##############################################################################################        AdminGrp Views END        ###########################################################################################


   
##############################################################################################      FinanceGrp Views:          ##############################################################################################


##############################################################################################      FinanceGrp Views: END          ###########################################################################################



   

      
##############################################################################################      QAPMC Grp   View       ##############################################################################################

class ManageQAPMCGrpListView(LoginRequiredMixin,ListView):
    model = QAPMCGrp
    template_name = 'manage_qapmcgrp.html'
    context_object_name = 'qapmc_list'
    def get_queryset(self):
        queryset = QAPMCGrp.objects.all()
        asset_identifier = self.request.GET.get('asset_identifier', None)
        if asset_identifier:
            queryset = queryset.filter(asset_identifier__icontains=asset_identifier)
        return queryset

class ManageQAPMCGrpCreateView(LoginRequiredMixin,CreateView):
    model = QAPMCGrp
    form_class = QapmcGrpForm  # You should create a form for QAPMCGrp (QAPMCGrpForm)
    template_name = 'manage_qapmcgrp.html'
    success_url = reverse_lazy('manage_qapmc')  # Redirect to the list view upon successful creation

class ManageQAPMCGrpUpdateView(LoginRequiredMixin,UpdateView):
    model = QAPMCGrp
    form_class = QapmcGrpForm  # You should create a form for QAPMCGrp (QAPMCGrpForm)
    template_name = 'manage_qapmcgrp.html'
    success_url = reverse_lazy('manage_qapmc')  # Redirect to the list view upon successful update

class ToggleQAPMCGrpStatusView(LoginRequiredMixin,View):
    def post(self, request, *args, **kwargs):
        asset_id = kwargs.get('asset_id')
        asset = get_object_or_404(QAPMCGrp, pk=asset_id)

        # Toggle the status
        if asset.status == 'A':
            asset.status = 'I'
            messages.success(request, f"Asset '{asset.owner}' has been deactivated.")
        else:
            asset.status = 'A'
            messages.success(request, f"Asset '{asset.owner}' has been activated.")

        # Save the changes and redirect
        asset.save()
        return redirect('manage_qapmc')  # Redirect back to the list view

##############################################################################################       QAPMC Grp   View  END         ###########################################################################################
def handle_group_data(df, group_name):
    """
    Handles the processing and saving of group data from a DataFrame to a database model.

    Args:
        df (pd.DataFrame): The DataFrame containing the data to be processed.
        group_name (str): The group name corresponding to the model to save the data.

    Raises:
        ValueError: If the group name is invalid.
    """
    # Define required columns
    required_columns = [
        'Asset Type', 'Asset Name', 'Asset Identifier', 'Owner', 'Custodian',
        'User', 'Asset Group', 'Location',
        'Security Classification', 'AMC/Warranty End Date', 'Backup Location'
    ]

    # Retain only the required columns; fill missing ones with NaN
    for col in required_columns:
        if col not in df.columns:
            df[col] = ''

    # Restrict the DataFrame to only required columns
    df = df[required_columns]

    # Remove rows where all values are NaN or empty
    df = df.dropna(how='all')  # Drops rows where all columns are NaN
    df = df[~df.apply(lambda x: x.str.strip().eq('').all(), axis=1)]  # Drops rows with all empty strings

    # Define a dictionary mapping group names to model classes
    group_models = {
        'ICTSGrp': ICTSGrp,
        'AEEGrp': AEEGrp,
        'ASPGGrp': ASPGGrp,
        'STGGrp': ETGGrp,
        'SSAGrp': SSAGrp,
        'QAPMCGrp': QAPMCGrp,
    }

    # Get the appropriate model based on the selected group
    model = group_models.get(group_name)
    if not model:
        raise ValueError(f"Invalid group selected: {group_name}")

    # Prepare objects for bulk insertion
    objects_to_create = []

    # Process each row and create model instances
    for index, row in df.iterrows():
        try:
            # Parse date fields with error handling for invalid dates
            amc_warranty_end_date = None
            if row['AMC/Warranty End Date']:
                try:
                    # Convert to datetime, coerce errors to NaT (Not a Time)
                    amc_warranty_end_date = pd.to_datetime(
                        row['AMC/Warranty End Date'], errors='coerce'
                    )
                    if pd.isna(amc_warranty_end_date):
                        amc_warranty_end_date = None  # Handle invalid date as None
                except Exception as date_error:
                    print(f"Error parsing date for row {index}: {date_error}")
                    amc_warranty_end_date = None

            # Create an object for the model
            obj = model(
                asset_type=row['Asset Type'].strip(),
                asset_name=row['Asset Name'].strip(),
                asset_identifier=row['Asset Identifier'].strip(),
                owner=row['Owner'].strip(),
                custodian=row['Custodian'].strip(),
                user=row['User'].strip(),
                asset_group=row['Asset Group'].strip(),
                asset_location=row['Location'].strip(),
                security_classification=row['Security Classification'].strip(),
                amc_warranty_end_date=amc_warranty_end_date,
                backup_location=row['Backup Location'].strip(),
            )
            objects_to_create.append(obj)

        except Exception as row_error:
            print(f"Error processing row {index}: {row.to_dict()}, Error: {row_error}")
            continue

    # Bulk create objects
    if objects_to_create:
        try:
            model.objects.bulk_create(objects_to_create, batch_size=100)
            print(f"Successfully saved {len(objects_to_create)} records to the {group_name} group.")
        except Exception as bulk_error:
            print(f"Error during bulk creation: {bulk_error}")
            raise
    else:
        print("No valid records found to save.")




def upload_file(request):
    if request.method == 'POST':
        form = ExcelFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['file']
            group_name = form.cleaned_data['group']

            try:
                # Read the Excel file using pandas
                df = pd.read_excel(uploaded_file)

                # Debugging: Print the dataframe to ensure it's being read correctly
                print("Excel DataFrame:\n", df.head())

                # Process the Excel data for the selected group
                handle_group_data(df, group_name)

                # Redirect to a success page or data display view
                return redirect('super_admin_dashboard')

            except ValueError as e:
                # Log the error and add a form error
                print(f"Error processing Excel file: {e}")
                form.add_error(None, str(e))
            except Exception as e:
                # Catch any other exception
                print(f"Unexpected error: {e}")
                form.add_error(None, f"Error processing Excel file: {e}")
        else:
            print("Form is not valid:", form.errors)
    else:
        form = ExcelFileForm()

    return render(request, 'upload_excel.html', {'form': form})







class ManageAdminListView(LoginRequiredMixin,ListView):
    model = AdminGrp
    template_name = 'manage_admingrp.html'
    context_object_name = 'admin_list'

class ManageFinanceListView(LoginRequiredMixin,ListView):
    model = FinanceGrp
    template_name = 'manage_financegrp.html'
    context_object_name = 'finance_list'