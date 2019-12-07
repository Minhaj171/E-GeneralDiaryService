from django.shortcuts import render


# Create your views here.

def showvictim(request):
    return render(request, "index.html")
def loginPage(request):
    return render(request, "login.html")

