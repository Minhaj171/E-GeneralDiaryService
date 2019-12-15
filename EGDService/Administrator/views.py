from django.shortcuts import render
from victim.models import Complain


def adminHome(request):
    return render(request, "administrator/DashBoard.html")


def showComplain(request):
    c = Complain.objects.all()
    return render(request, 'administrator/view_complain.html', {'complainlist': c})
