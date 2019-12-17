from django.shortcuts import render, redirect
from policeOfficer.models import police
from .models import user_reg

# Create your views here.
# def show_index(request):
# return render(request, "logged_in/index.html")
from Administrator.models import adminn


def show_log(request):
    return render(request, "logged_in/Log_in.html")


def User_registration(request):
    if request.method == 'POST':
        user_create = user_reg.objects.create(user_name=request.POST['username'], user_phone=request.POST['phone'],
                                              user_email=request.POST['email'], user_password=request.POST['psw'])
        user_create.save()
        return render(request, 'logged_in/Log_in.html')
    else:
        return render(request, 'logged_in/Signup_form.html')


def userlogin(request):
    if request.method == 'POST':
        uselect = request.POST['userselect']
        if uselect == "User":
            mail = request.POST['email']
            upass = request.POST['password']
            loggedin = user_reg.objects.filter(user_email=mail, user_password=upass)
            if loggedin:
                return render(request, 'u_victim/user_dashboard.html')
        elif uselect == "Police":
            mail = request.POST['email']
            upass = request.POST['password']
            loggedin = police.objects.filter(email=mail, password=upass)
            if loggedin:
                request.session['police_email'] = mail
                return redirect('policeOfficer/')
            else:
                return render(request, "logged_in/Log_in.html")
        else:
            mail = request.POST['email']
            upass = request.POST['password']
            loggedin = adminn.objects.filter(email=mail, password=upass)
            if loggedin:
                return redirect('Administrator/')
