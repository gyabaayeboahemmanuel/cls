from django.shortcuts import render
from .forms import *
# Create your views here.
def allocate(request):
    if request.method == "POST":
        allocationform = AllocationForm(data=request.POST, files=request.FILES)
        if allocationform.is_valid:
            allocationform.save()
            print(".................... saving was succefull...............")
            messages.success(request, 'user created')
        else:
            print("........Error form not vilid.......")
            messages.success(request, 'user created')
    else:
        allocationform = AllocationForm()
        print("nothing came out")
    context = {
       "allocationform":allocationform
    }
    return render(request, "make_allocations.html", context )