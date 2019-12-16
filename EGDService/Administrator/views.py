from django.contrib import messages
from django.shortcuts import render
from victim.models import Complain
from tourist.models import PoliceVerification

from .models import policeComplain


def adminHome(request):
    return render(request, "administrator/DashBoard.html")


def showComplain(request):
    c = Complain.objects.all()
    return render(request, 'administrator/view_complain.html', {'complainlist': c})


def ShowVerification(request):
    p = PoliceVerification.objects.all()
    return render(request, 'administrator/view_verifications.html', {'verificationlist': p})


def sendComplain(request, id):  # send complain to police-2
    sc = Complain.objects.get(id=id)
    multiple_complain = policeComplain.objects.filter(id=id)
    if multiple_complain:
        messages.success(request, "This complain is already sent!")
        return showComplain(request)
    else:
        policeComplain.objects.create(id=sc.id, Complain_type=sc.Complain_type,
                                      Complainant_name=sc.Complainant_name, Mobile_Number=sc.Mobile_Number,
                                      National_id=sc.National_id, District=sc.District,
                                      Thana=sc.Thana,
                                      Address=sc.Address, Complain_description=sc.Complain_description,
                                      Email=sc.Email)
        messages.success(request, "Complain Send to Police Successfully!")
        return showComplain(request)
