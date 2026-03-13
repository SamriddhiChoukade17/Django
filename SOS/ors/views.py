from django.http import HttpResponse
from django.shortcuts import render, redirect

from .service.user_service import UserService


def test_ors(request):
    return HttpResponse("<h1>Testing ORS<h1/>")


def welcome(request):
    return render(request, 'welcome.html')


def user_signup_test(request):
    print(request.GET.get('firstName'))
    print(request.GET.get('lastName'))
    print(request.GET.get('loginId'))
    print(request.GET.get('password'))
    print(request.GET.get('dob'))
    print(request.GET.get('address'))
    return render(request, 'registration.html')



def user_signup(request):
    # print(request.POST.get('firstName'))
    # print(request.POST.get('lastName'))
    # print(request.POST.get('loginId'))
    # print(request.POST.get('password'))
    # print(request.POST.get('dob'))
    # print(request.POST.get('address'))
    # print(request.POST.get('csrfmiddlewaretoken'))

    message = ""
    if request.method == "POST":
        params = {}
        params['firstName'] = request.POST.get('firstName')
        params['lastName'] = request.POST.get('lastName')
        params['loginId'] = request.POST.get('loginId')
        params['password'] = request.POST.get('password')
        params['dob'] = request.POST.get('dob')
        params['address'] = request.POST.get('address')
        service = UserService()
        service.add(params)
        message = "User Registered Successfully..!!"
    return render(request, 'registration.html', {'message': message})

    #return render(request, "registration.html")

def user_signin(request):
    if request.method == "POST":
        if request.POST.get('operation')=="signIn":
            print(request.POST.get('loginId'))
            print(request.POST.get('password'))
        if request.POST.get('operation')=="signUp":
            #ye niche wala "/signup/" bad me pag ko directly access krne ke liye h. link se directly access hoga and we don't be needing to type "*ors/signup"
            return redirect("/signup/")
            #return redirect("ors/signup/")

    return render(request, 'login2.html')

