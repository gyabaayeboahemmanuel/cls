from django.shortcuts import render
app_name = "land"
from .forms import *
# Create your views here.
def add_land(request):
    if request.method == "POST":
        landform = LandForm(data=request.POST, files=request.FILES)
        if landform.is_valid:
            landform.save()
            print(".................... saving was succefull...............")
        else:
            print("........Error form not vilid.......")
    else:
        landform = LandForm()
        print("nothing came out")
    context = {
       "landform": landform
    }
    return render(request, "add_land.html", context )
