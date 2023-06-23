from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model, login, authenticate
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import datetime
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
    # if login_form.username.is_superuser 
    return redirect('accounts/login')

def login_sucess(request):
    if not request.user.caretakerchief.exists():    
          return redirect("admin_dashboard")
    else:
        return redirect("chief_dashboard")
@login_required
def admindashboard(request):
    username = request.user.username
    chiefs = CareTakerChief.objects.all()
    staff = User.objects.all()
    land = Land.objects.all()
    client = Client.objects.all()
    allocation = Allocation.objects.all()
    active= "active bg-gradient-primary"
    april = "2023-05-14"
  

    d_today = datetime.datetime.now()
    d_day = d_today.day
    d_month = d_today.month
    year= d_today.year
    print("==========================")
    print(year)
    # if d_day > 7:
    #     day = d_day % 7


    jan = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=1).count()
    feb = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=2).count()
    mar = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=3).count()
    apr = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=4).count()
    may = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=5).count()
    jun = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=6).count()
    jul = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=7).count()
    aug = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=8).count()
    sept = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=9).count()
    octo = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=10).count()
    nov = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=11).count()
    dec = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=12).count()
  
  
    mon = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=d_month, dateofallocation__day=d_day).count()
    tues = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=d_month, dateofallocation__day=d_day-1).count()
    wed = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=d_month, dateofallocation__day=d_day-2).count()
    thurs = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=d_month, dateofallocation__day=d_day-3).count()
    fri = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=d_month, dateofallocation__day=d_day-4).count()
    sat = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=d_month, dateofallocation__day=d_day-5).count()
    sun = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=d_month, dateofallocation__day=d_day-6).count()
   

    context = {
    "jan": jan,
    "feb": feb,
    "mar": mar,
    "apr": apr,
    "may": may,
    "jun": jun,
    "jul": jul,
    "aug": aug,
    "sept": sept,
    "oct": octo,
    "nov": nov,
    "dec": dec,


    "mon" :mon,
    "tues" :tues,
    "wed" :wed,
    "thurs" :thurs,
    "fri" :fri,
    "sat" :sat,
    "sun" :sun,

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
def chief_dashboard(request):
    username = request.user.username
    chiefs = CareTakerChief.objects.all()
    staff = User.objects.all()
    land = Land.objects.all()
    client = Client.objects.all()
    allocation = Allocation.objects.all()
    active= "active bg-gradient-primary"
    april = "2023-05-14"
    year= 2023
    day = 1

    d_today = datetime.datetime.now()
    w_day = d_today.strftime("%a")
    # print(w_day)
    d_day = d_today.day
    month_m = d_today.month
    # print("==========================")
    # print(d_day)
    if d_day > 7:
        day = d_day % 7

    jan = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=1).count()
    feb = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=2).count()
    mar = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=3).count()
    apr = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=4).count()
    may = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=5).count()
    jun = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=6).count()
    jul = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=7).count()
    aug = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=8).count()
    sept = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=9).count()
    octo = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=10).count()
    nov = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=11).count()
    dec = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=12).count()
  
    wk1 = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=month_m, dateofallocation__day__gte=1, dateofallocation__day__lte=7).count()
    wk2 = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=month_m, dateofallocation__day__gte=8,  dateofallocation__day__lte=14).count()
    wk3 = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=month_m, dateofallocation__day__gte=15,  dateofallocation__day__lte=21).count()
    wk4 = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=month_m, dateofallocation__day__gte=22,  dateofallocation__day__lte=28).count()
    wk5 = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=month_m, dateofallocation__day__gte=29, dateofallocation__day__lte=31).count()
   
    context = {
    "jan": jan,
    "feb": feb,
    "mar": mar,
    "apr": apr,
    "may": may,
    "jun": jun,
    "jul": jul,
    "aug": aug,
    "sept": sept,
    "oct": octo,
    "nov": nov,
    "dec": dec,

    "wk1" :wk1,
    "wk2" :wk2,
    "wk3" :wk3,
    "wk4" :wk4,
    "wk5" :wk5,

    
    "username":username,
    "chief_data":chiefs,
    "staff_data":staff,
    "land_data":land,
    "client_data": client,
    "allocation_data":allocation,
    "active1":active,
    }
    return render(request, "online/chief_dashboard.html",context )
@login_required
def chief_statistics(request):
    username = request.user.username
    chiefs = CareTakerChief.objects.all()
    staff = User.objects.all()
    land = Land.objects.all()
    client = Client.objects.all()
    allocation = Allocation.objects.all()
    active= "active bg-gradient-primary"
    april = "2023-05-14"
    year= 2023
    day = 1

    d_today = datetime.datetime.now()
    w_day = d_today.strftime("%a")
    print(w_day)
    d_day = d_today.day
    month_m = d_today.month
    print("==========================")
    print(d_day)
    if d_day > 7:
        day = d_day % 7

    jan = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=1).count()
    feb = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=2).count()
    mar = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=3).count()
    apr = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=4).count()
    may = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=5).count()
    jun = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=6).count()
    jul = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=7).count()
    aug = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=8).count()
    sept = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=9).count()
    octo = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=10).count()
    nov = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=11).count()
    dec = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=12).count()
  
    wk1 = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=month_m, dateofallocation__day__gte=1, dateofallocation__day__lte=7).count()
    wk2 = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=month_m, dateofallocation__day__gte=8,  dateofallocation__day__lte=14).count()
    wk3 = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=month_m, dateofallocation__day__gte=15,  dateofallocation__day__lte=21).count()
    wk4 = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=month_m, dateofallocation__day__gte=22,  dateofallocation__day__lte=28).count()
    wk5 = Allocation.objects.filter(dateofallocation__year=year, dateofallocation__month=month_m, dateofallocation__day__gte=29, dateofallocation__day__lte=31).count()
   
    context = {
    "jan": jan,
    "feb": feb,
    "mar": mar,
    "apr": apr,
    "may": may,
    "jun": jun,
    "jul": jul,
    "aug": aug,
    "sept": sept,
    "oct": octo,
    "nov": nov,
    "dec": dec,

    "wk1" :wk1,
    "wk2" :wk2,
    "wk3" :wk3,
    "wk4" :wk4,
    "wk5" :wk5,

    
    "username":username,
    "chief_data":chiefs,
    "staff_data":staff,
    "land_data":land,
    "client_data": client,
    "allocation_data":allocation,
    "active1":active,
    }
    return render(request, "online/chief_statistics.html",context )

@login_required
def allocation_chit(request):
    allocationchit = AllocationChit.objects.all()
    context={
        "allocation_chits":allocationchit
    }
    return render(request, "online/allocation_chit.html", context)
@login_required
def add_allocation_chit(request):
    allocationchitform = AllocationChitForm(data=request.POST)
    chiefuser = request.user

    user = get_object_or_404(CareTakerChief, id = chiefuser.id)
    print(chiefuser.id)
    if request.method == "POST": 
        if allocationchitform.is_valid:
           chitform= allocationchitform.save(commit=False)
           chitform.CareTakerChief =user
           chitform.save()
    context = {
        "chitform":allocationchitform,
    }
    return render(request, "online/add_allocation_chit.html", context)
@login_required
def edit_allocation_chit(request):
    return render(request, "online/edit_allocation_chit.html")


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
        userform = StaffForm(data=request.POST, files=request.FILES)
        if chiefform.is_valid and userform.is_valid:
            try:
                userform.save()
                print("..................saving was succeful...............")
                messages.success(request, '------------------------------- Staff Sucessfully added')
                return redirect(admin_chief_records)
            except:
                print("..................saving was succeful...............")
                messages.error(request, '------------------------------------------------------------------------------⚠️--Error: Username Already Used for another staff')
        else:
            print("........Error form not vilid.......")
            #messages.success(request, 'user created')
            userform.save()
            chiefform.save(commit=False)
            print("..................saving was succeful...............")
            return redirect(admin_chief_records)
    else:
        userform = StaffForm()
        chiefform = ChiefForm()
        print("nothing came out")
    active= "active bg-gradient-primary"
    context = {
       "userform":userform,
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
def admin_update_staff_profile(request, username):
    if not Profile.objects.filter(user__username=username):
        print("user does not exited : Procede to create account ")
        profile = Profile.objects.create(user_username=username)
    user1 = get_object_or_404(Profile, user__username = username)
    username1 = username
    
    if request.method == "POST":
        staffprofileform = UserProfileForm(data=request.POST, files=request.FILES, instance= user1)
        if staffprofileform.is_valid:
            # 
            #     print("====================== Profile created ")

            # staffprofile = staffprofileform.save(commit=False)
            # print("................geky")
            # # staffprofile.user = username1
            # profile = Profile.objects.create(user=username1)
            
            staffprofileform.save()
            print("................geky")
            print("..................saving was succeful...............")
            return redirect(admin_staff_records)
            #messages.success(request, 'user created')
        else:
            print("........Error form not vilid.......")
            #messages.success(request, 'user created')
    else:
        staffprofileform = UserProfileForm()
        print("nothing came out")
    active= "active bg-gradient-primary"
    context = {
       "staffform":staffprofileform,
        "username":username,
    "active5":active,
    }
    return render(request, "online/update_staff.html", context )

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
    no_record_check = 1

    if request.method == "POST":
        landform = LandForm(data=request.POST, files=request.FILES)
        if landform.is_valid: 
            landinfo = landform.save(commit=False)
            landinfo.uniqueLandId = landinfo.plot + landinfo.block + landinfo.sector
            try:
                landinfo.save()
                messages.success(request, '--------------------------------------------------------------------------------✅Land Successfully Registered...............')
                return redirect(admin_land_records)
            except:
                print("..................saving was succeful...............")
                messages.error(request, '------------------------------------------------------------------------------⚠️Error: Land Already Registered')
                no_record_check = 0 
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
        "no_record_check":no_record_check,
    }
    return render(request, "online/add_landrecords.html", context )
@login_required
def admin_edit_land(request, id):
    land = get_object_or_404(Land, pk=id)
    username = request.user.username
    no_record_check = 0
    if request.method == "POST":
        landform = LandForm(data=request.POST, files=request.FILES, instance=land)
        if landform.is_valid: 
            landinfo = landform.save(commit=False)
            landinfo.uniqueLandId = landinfo.plot + landinfo.block + landinfo.sector
            try:
                landinfo.save()
                messages.success(request, '--------------------------------------------------------------------------------✅Land Successfully Registered...............')
                no_record_check = 0
            except:
                print("..................saving was succeful...............")
                messages.error(request, '------------------------------------------------------------------------------⚠️--Error: Land Already Registered')
                no_record_check = 1
           
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
        "no_record_check":no_record_check,
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
        clientform = ClientForm(data=request.POST, files = request.FILES, instance=allocation)
        if clientform.is_valid:
            clientform.save()
            return redirect(admin_client_records)
        else: 
            print("Invalid data entry")
    else:
        clientform = ClientForm(instance=client)
    active= "active bg-gradient-primary"
    context = {
       "clientform":clientform,
       "id":id,
        "username":username,
        "active3":active,
    }
    return render(request, "online/add_client.html", context )

    


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