from django.shortcuts import render, redirect

from .models import PoliceVerification


# Create your views here.
def show_index(request):
    return render(request, "login.html")


def user_ver(request):
    if request.method == "POST":
        p = PoliceVerification(Tourist_name=request.POST['T_name'],
                               C_tourist=request.POST['T_Countrey'],
                               Tourist_M=request.POST['T_mobile'],
                               Tourist_Email=request.POST['T_email'],
                               Tourist_duration=request.POST['T_duration'],
                               Passport_id=request.POST['T_pid'])
        p.save()
    return render(request, "P_Verification.html")
