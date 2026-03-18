from django.http import HttpResponse
from django.shortcuts import render, redirect

from .service.marksheet import MarksheetService
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
    # if request.method == "POST":
    #     if request.POST.get('operation')=="signIn":
    #         print(request.POST.get('loginId'))
    #         print(request.POST.get('password'))
    #     if request.POST.get('operation')=="signUp":
    #         #ye niche wala "/signup/" bad me pag ko directly access krne ke liye h. link se directly access hoga and we don't be needing to type "*ors/signup"
    #         return redirect("/signup/")
    #         #return redirect("ors/signup/")
    #
    # return render(request, 'login2.html')


    message = ''
    if request.method == "POST":
        if request.POST.get('operation') == "signIn":
            loginId = request.POST.get('loginId')
            password = request.POST.get('password')
            service = UserService()
            user_data = service.auth(loginId, password)
            if len(user_data) != 0:
                request.session['firstName'] = user_data[0].get('firstName')
                return redirect('/')
                # return render(request, 'welcome.html', {'firstName': user_data[0].get('firstName')})
            else:
                message = 'Login ID & Password Invalid'
        if request.POST.get('operation') == "signUp":
            return redirect("/signup/")
    return render(request, 'login2.html', {'message': message})


def logout(request):
    request.session['firstName'] = None
    return redirect('/signin')


def test_list(request):
    list = [
        {"id": 1, "firstName": "abc", "lastName": "aaa", "email": "abc@gmail.com", "password": "12345"},
        {"id": 2, "firstName": "xyz", "lastName": "aaa", "email": "abc@gmail.com", "password": "12345"},
        {"id": 3, "firstName": "pqr", "lastName": "aaa", "email": "abc@gmail.com", "password": "12345"}
    ]
    return render(request, "testlist.html", {"list": list})


def user_list(request):
    params = {}
    params['pageNo'] = 1
    params['pageSize'] = 5

    service = UserService()
    list = service.search(params)

    return render(request, 'userlist.html', {"list": list, 'pageNo': params['pageNo']})


def marksheet(request):
    message = ""
    if request.method == "POST":
        params = {}
        params['fullName'] = request.POST.get('fullName')
        params['rollNo'] = request.POST.get('rollNo')
        params['physics'] = request.POST.get('physics')
        params['chemistry'] = request.POST.get('chemistry')
        params['maths'] = request.POST.get('maths')
        service = MarksheetService()
        service.add(params)
        message = "Student Registered Successfully..!!"

    return render(request,'marksheet.html', {'message': message})

def add_user(request):
    message = ""
    if request.method == "POST":
        params = {}
        params['firstName'] = request.POST.get('firstName')
        params['lastName'] = request.POST.get('lastName')
        params['loginId'] = request.POST.get('loginId')
        params['password'] = request.POST.get('password')
        params['dob'] = request.POST.get('dob')
        params['address'] = request.POST.get('address')
        # service = UserService()
        # service.add(params)
        # message = "User Registered Successfully..!!"
    return render(request, 'adduser.html', {'message': message})