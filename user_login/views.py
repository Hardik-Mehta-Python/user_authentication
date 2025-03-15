from django.shortcuts import render,HttpResponse,redirect
from .models import Sign_up
from django.contrib import messages

# Create your views here.
def index(request):
    
    return render(request,"index.html")
    

def login(request):
    if request.method == "POST":
        try:
            user = Sign_up.objects.get(
                username = request.POST['username'],
                password = request.POST['password'],
                )
            request.session['username'] = user.username
            return redirect(index)
        except:
            return render(request,"login.html")
    else:
        return render(request,"login.html")

def signup(request):
    if request.method == "POST":
        name = request.POST["name"]
        username = request.POST["username"]
        email = request.POST["email"]
        Phonenumber = request.POST["Phonenumber"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if Sign_up.objects.filter(username = username).exists():
            messages.error(request,"username already taken")
            return redirect(signup)
        if password != confirm_password :
            messages.error(request,"password does not match")
            return redirect(signup)
        data = Sign_up(name = name, username=username,email=email,Phonenumber=Phonenumber,password=password,confirm_password=confirm_password)
        data.save()
        return redirect(login)

    else:
        return render(request,"signup.html")



    # return render(request,"signup.html")

