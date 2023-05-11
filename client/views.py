from django.shortcuts import render

from .forms import *
# Create your views here.
def add_client(request):
    if request.method == "POST":
        clientform = ClientForm(data=request.POST, files=request.FILES)
        if clientform.is_valid:
            clientform.save()
            print(".................... saving was succefull...............")
        else:
            print("........Error form not vilid.......") 
    else:
        clientform = ClientForm()
        print("nothing came out")
    context = {
       "clientform":clientform
    }
    return render(request, "add_client.html", context )