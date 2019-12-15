from django.shortcuts import render


# Create your views here.
def Show_officer_Dash(request):
    return render(request, "policeofficer/PDashBoard.html")


def ShowCrimes(request):
    return render(request, "policeofficer/crime.html")


def Show_ver_requests(request):
    return render(request, "policeofficer/verification_requests.html")