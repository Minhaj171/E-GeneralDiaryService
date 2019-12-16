from django.contrib import messages
from django.shortcuts import render

from victim.models import Complain

from Administrator.models import policeComplain
from .models import police


def Show_officer_Dash(request):
    return render(request, "policeofficer/PDashBoard.html")


def ShowCrimes(request):
    po = police.objects.get(email=request.session.get('police_email'))
    obj = policeComplain.objects.filter(Thana=po.thana)
    context = {'complain': obj}
    return render(request, "policeofficer/crime.html", context)


def Show_ver_requests(request):
    return render(request, "policeofficer/verification_requests.html")

def police_reg(request):
    if request.method == 'POST':
        check_thana = police.objects.filter(thana = request.POST['thana'])
        if check_thana:
            messages.success(request, "This Police is already registered!!")
            return render(request, 'policeofficer/p_registration.html')
        else:
            police_create = police.objects.create(name=request.POST['pname'], email = request.POST['pemail'], password = request.POST['password'], phone = request.POST['phone'],thana = request.POST['thana'])
            police_create.save()
            messages.success(request, "Police Account Created!")
            return  render(request, 'policeofficer/p_registration.html')
    else:
        return  render(request, 'policeofficer/p_registration.html')