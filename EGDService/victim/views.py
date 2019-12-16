from django.shortcuts import render, redirect
from .models import Complain


# Create your views here.

def userPage(request):
    return render(request, "user_dashboard.html")


#def call_complain(request):
 #   return render(request, "u_victim/complain.html")


def userComplain(request):
    if request.method == 'POST':
        c = Complain(Complain_type=request.POST['Complaint_type'],
                     Complainant_name=request.POST['name'], Mobile_Number=request.POST['mobile'],
                     National_id=request.POST['identity_id'], District=request.POST['District'],
                     Thana=request.POST['Thana'],
                     Address=request.POST['address'], Complain_description=request.POST['Y_complain'],
                     Email=request.POST['email'])
        c.save()
        return render(request, "u_victim/complain.html")
    else:
        return render(request, "u_victim/complain.html")
