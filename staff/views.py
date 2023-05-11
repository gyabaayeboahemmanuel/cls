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

def indexview(request):
    return render(request,"index.html")

def loginIndex(request):
    login_form = User
    context = {
        "login_form":login_form,
    }
    return render(request, "online/sign-in.html")

@login_required
def admindashboard(request):
    return render(request, "online/dashboard.html")

@login_required
def admin_chief_records(request):
    loginedid = request.user
    chiefs = CareTakerChief.objects.all()
    context= {
        "chief_data":chiefs,
        "loginedid":loginedid,
    }
    return render(request, "online/chiefs_records.html", context)

@login_required
def admin_add_chief(request):
    if request.method == "POST":
        chiefform = ChiefForm(data=request.POST, files=request.FILES)
        if chiefform.is_valid:
            chiefform.save()
            print("..................saving was succeful...............")
        else:
            print("........Error form not vilid.......")
    else:
        chiefform = ChiefForm()
        print("nothing came out")
    context = {
       "chiefform":chiefform
    }
    return render(request, "online/add_chief.html", context )

@login_required
def admin_edit_chief(request, id): 
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
    context = {
       "chiefform":chiefform,
       "id":id,
    }
    return render(request, "online/edit_chief.html", context )

@login_required
def admin_view_chief(request, id):
    chief = get_object_or_404(CareTakerChief, pk=id)
    context={
        "chief":chief
    }
    return render(request, "online/chief_details.html")

@login_required
def admin_delete_chief(request, id):
    chief = get_object_or_404(CareTakerChief, pk=id )
    chief.delete()
    return redirect(admin_chief_records)

        
@login_required
def admin_staff_records(request):
    staff = User.objects.all()
    search_item = request.GET.get('search_item')
    if search_item != '' and search_item != None:
        staff = staff.filter(title__icontains = search_item)
        
    context= {
        "staff_data":staff,
    }
    return render(request, "online/staff_records.html", context)

@login_required
def admin_add_staff(request):
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
    context = {
       "staffform":staffform,
               "username":username,
    }
    return render(request, "online/add_staff.html", context )

@login_required
def admin_staff_profile(request, username):
    username = request.user.username
    staff = get_object_or_404(User, username = request.user)
    # staff = get_object_or_404(Profile, user=username)     
    context= {
        "staff_data":staff,
        "username":username,
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
    context = {
       "staffform":staffform,
        "username":username,
    }
    return render(request, "online/add_staff.html", context )

@login_required
def admin_add_land(request):
    username = request.user.username
    if request.method == "POST":
        landform = LandForm(data=request.POST, files=request.FILES)
        if landform.is_valid:
            landform.save()
            print("..................saving was succeful...............")
            #messages.success(request, 'user created')
            return redirect(admin_land_records)
        else:
            print("........Error form not vilid.......")
            #messages.success(request, 'user created')
    else:
        landform = LandForm()
        print("nothing came out")
    context = {
       "landform":landform,
        "username":username,
    }
    return render(request, "online/add_landrecords.html", context )

@login_required
def admin_land_records(request):
    username = request.user.username
    land = Land.objects.all()
    context= {
        "land_data":land, "username":username,

    }
    return render(request, "online/land_records.html", context)

@login_required
def admin_client_records(request):
    username = request.user.username
    client = Client.objects.all()
    context= {
        "client_data":client,
        "username":username,
    }
    return render(request, "online/client_records.html", context)

@login_required
def admin_add_client(request):
    username = request.user.username
    if request.method == "POST":
        clientform = ClientForm(data=request.POST, files=request.FILES)
        if clientform.is_valid:
            clientform.save()
            print("..................saving was succeful...............")
            #messages.success(request, 'user created')
        else:
            print("........Error form not vilid.......")
            #messages.success(request, 'user created')
    else:
        clientform = ClientForm()
        print("nothing came out")
    context = {
       "clientform":clientform,
        "username":username,
    }
    return render(request, "online/add_client.html", context )

@login_required
def admin_allocation_records(request):
    username = request.user.username
    allocation = Allocation.objects.all()
    context= {
        "allocation_data":allocation,
        "username":username,
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
    context = {
       "allocationform":allocationform,
        "username":username,
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
    context = {
       "allocationform":allocationform,
       "id":id,
        "username":username,
    }
    return render(request, "online/edit_allocation.html", context )

@login_required
def admin_view_allocation(request, id):
    username = request.user.username
    allocation = get_object_or_404(Allocation, pk=id)
    context={
        "allocation":allocation,
        "username":username,
    }
    return render(request, "online/allocation_details.html")

@login_required
def admin_delete_allocation(request, id):
    allocation = get_object_or_404(Allocation, pk=id )
    allocation.delete()
    return redirect(admin_allocation_records)