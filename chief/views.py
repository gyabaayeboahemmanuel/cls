from django.shortcuts import render
from .forms import *
# Create your views here.
def add_chief(request):
    if request.method == "POST":
        chiefform = ChiefForm(data=request.POST, files=request.FILES)
        if chiefform.is_valid:
            chiefform.save()
            print(".................... saving was succefull...............")
            
        else:
            print("........Error form not vilid.......")
          
    else:
        chiefform = ChiefForm()
        print("nothing came out")
    context = {
       "chiefform": chiefform
    }
    return render(request, "add_chief.html", context )