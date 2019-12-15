from django.shortcuts import render
from victim.models import Complain
from tourist.models import PoliceVerification


def adminHome(request):
    return render(request, "administrator/DashBoard.html")


def showComplain(request):
    c = Complain.objects.all()
    return render(request, 'administrator/view_complain.html', {'complainlist': c})


def ShowVerification(request):
    p = PoliceVerification.objects.all()
    return render(request, 'administrator/view_verifications.html', {'verificationlist': p})