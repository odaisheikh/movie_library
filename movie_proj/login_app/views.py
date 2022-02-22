from django.shortcuts import render,redirect,HttpResponse
from .models import Login
from django.contrib import messages
import bcrypt

def login_form(request):
    return render(request,"login.html")

def register(request):
    request.session['flag'] = 'register'
    errors = Login.objects.basic_validator(request.POST)
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        request.session['email'] = request.POST['email']
        request.session['password'] = request.POST['password']
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash    
        print(pw_hash)
        Login.objects.create(first_name = request.POST['first_name'],last_name=request.POST['last_name']
        ,email=request.POST['email'],password=pw_hash,confirm_pw=pw_hash)
        return redirect("/")
    

def login(request):
    request.session['flag'] = 'login'
    request.session['email'] = request.POST['email']
    request.session['password'] = request.POST['password']
    # print(request.session['email'])
    # print(request.session['password'])
    loged_userx = Login.objects.filter(email = request.POST['email'])
    if(loged_userx):
        loged_user = Login.objects.get(email = request.POST['email'])
        # password = Login.objects.filter(password = request.session['password'])
        # print(email.email)
        # print(password.password)
        print(loged_user)
        context ={
            'name':loged_user.id
        }
        if bcrypt.checkpw(request.POST['password'].encode(), loged_user.password.encode()):
            if (loged_user.email == request.POST['email']):
                print(loged_user.email)
                return redirect('/main/'+str(loged_user.id))
    errors = Login.objects.check_login()
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
    # redirect the user back to the form to fix the errors
    return redirect('/')
    # return redirect('/')

def logout(request):
    del request.session['email']
    del request.session['password']
    return redirect('/')
