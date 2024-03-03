from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import registrationForm

def homePage(request):
    homePageData = {
        "pageTitle" : "Akeel Ahmad",
        "courses_list" : ["Boxing","Kick-Boxing","Grappling","Physical Fitness","Street Fighting"],
    }

    return render(request,"home.html",homePageData)

def aboutUs(request):
    return render(request,"aboutUs.html")

def services(request):
    return render(request,"services.html")

def formSubmitThankYou(request):
    if request.method == "POST":
        name = request.POST.get("fullName")
        return render(request,"formSubmitThankYou.html",{"name":name})
    else:
        return render(request,"formSubmitThankYou.html")
    

def registration(request):
    fn = registrationForm()
    data = {"form":fn}
    return render(request,"registration.html",data)

