from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model, login, authenticate
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

User = get_user_model()
from .forms import *
# Create your views here.
from chief.forms import *
from staff.forms import *
from lands.forms import *
from client.forms import *
from allocation.forms import *
from allocation.models import *
from staff.models import *
from lands.models import *
from client.models import *
from django.contrib import messages #import messages

def indexview(request):
    login_form = User
    context = {
        "login_form":login_form,
    }
    return render(request,"index.html",context )

def loginIndex(request):
    login_form = User
    
    context = {
        "login_form":login_form,
    }
    return redirect('accounts/login')

@login_required
def admindashboard(request):
    username = request.user.username
    chiefs = CareTakerChief.objects.all()
    staff = User.objects.all()
    land = Land.objects.all()
    client = Client.objects.all()
    allocation = Allocation.objects.all()
    active= "active bg-gradient-primary"
    context = {
    "username":username,
    "chief_data":chiefs,
    "staff_data":staff,
    "land_data":land,
    "client_data": client,
    "allocation_data":allocation,
    "active1":active,
    }
    return render(request, "online/dashboard.html",context )

@login_required
def admin_chief_records(request):
    username = request.user.username
    loginedid = request.user
    chiefs = CareTakerChief.objects.all()
    active= "active bg-gradient-primary"
    context= {
        "chief_data":chiefs,
        "username":username,
        "active6":active,
    }
    return render(request, "online/chiefs_records.html", context)

@login_required
def admin_add_chief(request):
    username = request.user.username
    if request.method == "POST":
        chiefform = ChiefForm(data=request.POST, files=request.FILES)
        if chiefform.is_valid:
            chiefform.save()
            print("..................saving was succeful...............")
            return redirect(admin_chief_records)
        else:
            print("........Error form not vilid.......")
    else:
        chiefform = ChiefForm()
        print("nothing came out")
    active= "active bg-gradient-primary"
    context = {
       "chiefform":chiefform,
        "username":username,
        "active6":active,
    }
    return render(request, "online/add_chief.html", context )

@login_required
def admin_edit_chief(request, id): 
    username = request.user.username
    chief = get_object_or_404(CareTakerChief, pk=id)
    if request.method == "POST":
        chiefform = ChiefForm(data=request.POST, files = request.FILES, instance=chief)
        if chiefform.is_valid:
            chiefform.save()
            return redirect(admin_chief_records)
        else: 
            print("Invalid data entry")
    else:
        chiefform = ChiefForm(instance=chief)
    active= "active bg-gradient-primary"
    context = {
       "chiefform":chiefform,
       "id":id,
               "username":username,
    "active6":active,     
    }
    return render(request, "online/edit_chief.html", context )

@login_required
def admin_view_chief(request, id):
    username = request.user.username
    chief = get_object_or_404(CareTakerChief, pk=id)
    active= "active bg-gradient-primary"
    context={
        "chief":chief,
                "username":username,
    "active6":active,
    }
    return render(request, "online/chief_details.html")

@login_required
def admin_delete_chief(request, id):
    chief = get_object_or_404(CareTakerChief, pk=id )
    chief.delete()
    return redirect(admin_chief_records)

        
@login_required
def admin_staff_records(request):
    username = request.user.username
    staff = User.objects.all()
    search_item = request.GET.get('search_item')
    if search_item != '' and search_item != None:
        staff = staff.filter(title__icontains = search_item)
    active= "active bg-gradient-primary" 
    context= {
    "staff_data":staff,
    "username":username,
    "active5":active,
    }
    return render(request, "online/staff_records.html", context)

@login_required
def admin_add_staff(request):
    username = request.user.username
    if request.method == "POST":
        staffform = StaffForm(data=request.POST, files=request.FILES)
        if staffform.is_valid:
            try:
                staffform.save()
                print("..................saving was succeful...............")
                messages.success(request, '------------------------------- Staff Sucessfully added')
                return redirect(admin_staff_records)
            except:
                print("..................saving was succeful...............")
                messages.error(request, '------------------------------------------------------------------------------⚠️--Error: Username Already Used for another staff')
        else:
            print("........Error form not vilid.......")
            #messages.success(request, 'user created')
    else:
        staffform = StaffForm()
        print("nothing came out")
    active= "active bg-gradient-primary"
    context = {
       "staffform":staffform,
        "username":username,
        "active5":active,
    }
    return render(request, "online/add_staff.html", context )

@login_required
def admin_staff_profile(request, username):
    username = request.user.username
    staff = get_object_or_404(User, username = request.user)
    # staff = get_object_or_404(Profile, user=username)    
    active= "active bg-gradient-primary"
    context= {
        "staff_data":staff,
        "username":username,
        "active5":active,
    }
    return render(request, "online/staff_profile.html", context)

@login_required
def admin_update_staff_profile(request):
    username = request.user.username
    if request.method == "POST":
        staffform = StaffForm(data=request.POST, files=request.FILES)
        if staffform.is_valid:
            staffform.save()
            print("..................saving was succeful...............")
            #messages.success(request, 'user created')
        else:
            print("........Error form not vilid.......")
            #messages.success(request, 'user created')
    else:
        staffform = StaffForm()
        print("nothing came out")
    active= "active bg-gradient-primary"
    context = {
       "staffform":staffform,
        "username":username,
    "active5":active,
    }
    return render(request, "online/add_staff.html", context )

@login_required
def admin_staff_activate(request, username):
    username1 = username
    staff = get_object_or_404(User, username = username1)
    print(staff.is_active)
    print(".........................")
    staff.is_active = True
    staff.save()
    return redirect(admin_staff_records)
@login_required
def admin_staff_deactivate(request, username):
    username1 = username
    staff = get_object_or_404(User, username = username1)
    print(staff.is_active)
    print(".........................")
    staff.is_active = False
    staff.save()
    return redirect(admin_staff_records)

@login_required
def admin_add_land(request):
    username = request.user.username
    if request.method == "POST":
        landform = LandForm(data=request.POST, files=request.FILES)
        if landform.is_valid: 
            landinfo = landform.save(commit=False)
            landinfo.uniqueLandId = landinfo.plot + landinfo.block + landinfo.sector
            try:
                landinfo.save()
                messages.success(request, '--------------------------------------------------------------------------------✅Land Successfully Registered...............')
            except:
                print("..................saving was succeful...............")
                messages.error(request, '------------------------------------------------------------------------------⚠️--Error: Land Already Registered')
            return redirect(admin_land_records)
        else:
            print("........Error form not vilid.......")
            #messages.success(request, 'user created')
    else:
        landform = LandForm()
        print("nothing came out")
    active= "active bg-gradient-primary"
    context = {
       "landform":landform,
        "username":username,
        "active2":active,
    }
    return render(request, "online/add_landrecords.html", context )
@login_required
def admin_edit_land(request, id):
    land = get_object_or_404(Land, pk=id)
    username = request.user.username
    if request.method == "POST":
        landform = LandForm(data=request.POST, files=request.FILES, instance=land)
        if landform.is_valid: 
            landinfo = landform.save(commit=False)
            landinfo.uniqueLandId = landinfo.plot + landinfo.block + landinfo.sector
            try:
                landinfo.save()
                messages.success(request, '--------------------------------------------------------------------------------✅Land Successfully Registered...............')
            except:
                print("..................saving was succeful...............")
                messages.error(request, '------------------------------------------------------------------------------⚠️--Error: Land Already Registered')
            return redirect(admin_land_records)
        else:
            print("........Error form not vilid.......")
            #messages.success(request, 'user created')
    else:
        landform = LandForm( instance=land)
        print("nothing came out")
    active= "active bg-gradient-primary"
    context = {
       "landform":landform,
        "username":username,
        "active2":active,
    }
    return render(request, "online/add_landrecords.html", context )

@login_required
def admin_land_records(request):
    username = request.user.username
    land = Land.objects.all()
    active= "active bg-gradient-primary"
    context= {
        "land_data":land,
         "username":username,
        "active2":active,
    }
    return render(request, "online/land_records.html", context)

@login_required
def admin_client_records(request):
    username = request.user.username
    client = Client.objects.all()
    active= "active bg-gradient-primary"
    context= {
        "client_data":client,
        "username":username,
        "active4":active,
    }
    return render(request, "online/client_records.html", context)

@login_required
def admin_edit_client_records(request,id):
    client = get_object_or_404(Client, pk=id)
    if request.method == "POST":
        clientform = AllocationForm(data=request.POST, files = request.FILES, instance=allocation)
        if clientform.is_valid:
            clientform.save()
            return redirect(admin_client_records)
        else: 
            print("Invalid data entry")
    else:
        clientform = AllocationForm(instance=client)
    active= "active bg-gradient-primary"
    context = {
       "clientform":clientform,
       "id":id,
        "username":username,
        "active3":active,
    }
    return render(request, "online/edit_allocation.html", context )

    

@login_required
def admin_add_client(request):
    username = request.user.username
    if request.method == "POST":
        clientform = ClientForm(data=request.POST, files=request.FILES)
        if clientform.is_valid:
            clientform.save()
            print("..................saving was succeful...............")
            return redirect(admin_client_records)
            #messages.success(request, 'user created')
        else:
            print("........Error form not vilid.......")
            #messages.success(request, 'user created')
    else:
        clientform = ClientForm()
        print("nothing came out")
    active= "active bg-gradient-primary"
    context = {
       "clientform":clientform,
        "username":username,
        "active4":active,
    }
    return render(request, "online/add_client.html", context )

@login_required
def admin_allocation_records(request):
    username = request.user.username
    allocation = Allocation.objects.all()
    active= "active bg-gradient-primary"
    context= {
        "allocation_data":allocation,
        "username":username,
        "active3":active,
    }
    return render(request, "online/allocation_records.html", context)

@login_required
def admin_make_allocation(request):
    username = request.user.username
    if request.method == "POST":
        allocationform = AllocationForm(data=request.POST, files=request.FILES)
        if allocationform.is_valid:
            allocationform.save()
            print("..................saving was succeful...............")
            #messages.success(request, 'user created')
            return redirect(admin_allocation_records)
        else:
            print("........Error form not vilid.......")
            #messages.success(request, 'user created')
    else:
        allocationform = AllocationForm()
        print("nothing came out")
    active= "active bg-gradient-primary"
    context = {
        "allocationform":allocationform,
        "username":username,
        "active3":active,
    }
    return render(request, "online/make_allocation.html", context )

@login_required
def admin_edit_allocation(request, id): 
    username = request.user.username
    allocation = get_object_or_404(Allocation, pk=id)
    if request.method == "POST":
        allocationform = AllocationForm(data=request.POST, files = request.FILES, instance=allocation)
        if allocationform.is_valid:
            allocationform.save()
            return redirect(admin_allocation_records)
        else: 
            print("Invalid data entry")
    else:
        allocationform = AllocationForm(instance=allocation)
    active= "active bg-gradient-primary"
    context = {
       "allocationform":allocationform,
       "id":id,
        "username":username,
        "active3":active,
    }
    return render(request, "online/edit_allocation.html", context )

@login_required
def admin_view_allocation(request, id):
    username = request.user.username
    allocation = get_object_or_404(Allocation, pk=id)
    active= "active bg-gradient-primary"
    print(id)
    context={
        "allocation":allocation,
        "username":username,
    "active3":active,
    }
    return render(request, "online/allocation_details.html", context )

@login_required
def admin_delete_allocation(request, id):
    allocation = get_object_or_404(Allocation, pk=id )
    allocation.delete()
    return redirect(admin_allocation_records)