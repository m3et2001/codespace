from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .models import Profile, UserSignup, Thread ,Message
from django.contrib.auth.models import User
from django.http import JsonResponse
import uuid
import requests
import json
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q

# Create your views here.

def signin(request):
    if request.method == 'POST':
        print("login")
        print(request.POST)
        username_email = request.POST.get('email-phone')
        password = request.POST.get('password')

        user = authenticate(request, username=username_email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('chooseuser')
        else:
            try:
                user=User.objects.get(email=username_email)
                username=user.username
                print(username)
            except:
                print("user not available")
                messages.error(request, 'Wrong Credentials')
                return render(request,'account/login.html',)
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('chooseuser')
            else:
                messages.error(request, 'Wrong Credentials')
                return render(request,'account/login.html',)

    else:
        return render(request,'account/login.html')

def signup(request):
    if request.method == 'POST':
        print(request.POST)
        firstname=request.POST.get('first')
        lastname=request.POST.get('last')
        username=request.POST.get('username')
        print('this is username', username)
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirm_password')
        print(password)
        print(confirmpassword)
        DOB=request.POST.get('birthday')
        city=request.POST.get('city')
        state=request.POST.get('state')
        region=request.POST.get('region')
        male=request.POST.get('male')
        if not male:
            gender=request.POST.get('female')
        else:
            gender=male
        print(gender)
        if confirmpassword != password:
            print("password is not matching")
            messages.error(request, 'Password and Confirm Password are not matching!')
            return render(request, 'sign-up.html')
        else:
            request.session['username']=username
            request.session['firstname']=firstname
            request.session['lastname']=lastname
            request.session['email']=email
            request.session['gender']=gender
            request.session['DOB']=DOB
            request.session['state']=state
            request.session['city']=city
            request.session['region']=region
            request.session['password']=password
            uid=uuid.uuid4()
            pro_obj=Profile(user=username,token=uid)
            pro_obj.save()
            print(uid)
            send_mail_user(email,uid)
            messages.success(request,"We have sent you a confirmation mail,PLease verify your mail To complete your registration ")
            return redirect('signup')
            #ftc_user = UserSignup(Username=username,Firstname=firstname,Lastname=lastname,Email=email,Gender=gender,DOB=DOB,City=city,State=state,Region=region)
            #ftc_user.save()
            #user_object = User.objects.create_user(username=username, email=email,password=f'{password}')
            #user_object.save()
            #user=authenticate(request,username=username,password=password)
            
            #login(request,user)
            #print("user successfully created")
            #return render(request,'choose-user.html')
    else:
        return render(request,'sign-up.html')

def send_mail_user(email,token):

    subject="Confirmation Mail"
    print(token)
    message=f"Please click the link to verify your mail https://f-t-c.herokuapp.com/email-verification/{token}"
    from_email=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list)


def emailverification(request,token):
    #try:
    print(token)
    pf=Profile.objects.filter(token=token).first()
    if not pf.verify :
        pf.verify=True
        pf.save()
        print(pf.user)
        username=request.session.get('username')
        print('this is session', username)
        firstname=request.session.get('firstname')
        print('this is session', firstname)
        lastname=request.session.get('lastname')
        email=request.session.get('email')
        gender=request.session.get('gender')
        DOB=request.session.get('DOB')
        city=request.session.get('city')
        state=request.session.get('state')
        region=request.session.get('region')
        password=request.session.get('password')
        ftc_user = UserSignup(Username=username,Firstname=firstname,Lastname=lastname,Email=email,Gender=gender,DOB=DOB,City=city,State=state,Region=region)
        ftc_user.save()
        user_object = User.objects.create_user(username=username, email=email)
        user_object.set_password(password)
        user_object.save()
        print("user successfully created")
        print(request.session.get('username'))
        del request.session['username']
        del request.session['firstname']
        del request.session['lastname']
        del request.session['email']
        del request.session['gender']
        del request.session['DOB']
        del request.session['city']
        del request.session['state']
        del request.session['region']
        del request.session['password']
        user=authenticate(request,username=username,password=password)
            
        login(request,user)

        return redirect('chooseuser')
    # except Exception as e:
    #     print(e)
    else:
        return redirect('signin')


@login_required
def chooseuser(request):
    print("choosing user")
    username=request.user.username
    email=request.user.email
    user_availability=UserSignup.objects.filter(Email=email)
    if user_availability :
        user_obj=User.objects.all()
        print(user_obj)
        return render(request,"choose-user.html",{'user_obj':user_obj})
        #return redirect('chooseuser')
    else:
        return redirect('googleregister')

    
def check_username(request):
    print("username checking ")
    print(request.POST)
    print(request.POST['username'])
    user = request.POST['username']
    user_availability = User.objects.filter(username=user)
    if user_availability:
        status = 'not available'
    else:
        status = 'success'

    print(user_availability)
    print(status)
    return JsonResponse({'status': status})

def check_email(request):
    print("Email checking ")
    print(request.POST)
    print(request.POST['email'])
    email = request.POST['email']
    email_availability = User.objects.filter(email=email)
    if email_availability:
        status = 'not available'
    else:
        status = 'success'

    print(email_availability)
    print(status)
    return JsonResponse({'status': status})

def signout(request):
    logout(request)
    messages.success(request, 'Successfully logged out')

    return redirect('account_login')


def chatoption(request):

    return render(request,"Select_chat_option.html")

def googleregister(request):
    if request.method == 'POST':
        print("registering user")
        username=request.user.username
        email=request.user.email
        try:
            firstname=request.user.first_name
            lastname=request.user.last_name
        except:
            firstname=''
            lastname=''
        male=request.POST.get('male')
        if not male:
            gender=request.POST.get('female')
        else:
            gender=male
        DOB=request.POST.get('DOB')
        city=request.POST.get('city')
        state=request.POST.get('state')
        region=request.POST.get('region')
        
        user_object=UserSignup(Username=username,Firstname=firstname,Lastname=lastname,Email=email,Gender=gender,DOB=DOB,City=city,State=state,Region=region)
        user_object.save()
        return redirect('chooseuser')

    else:
        #redirect(provider_login_url 'google')
        print(request.user)
        username=request.user.username
        email=request.user.email
        user_availability=UserSignup.objects.filter(Email=email)
        if user_availability :
            return redirect('chooseuser')
        else:
            try:
                firstname=request.user.first_name
                print(firstname)
                lastname=request.user.last_name
            except:
                firstname=''
                lastname=''
            

            return render(request,"google_register_user.html",{'firstname':firstname,'lastname':lastname})


def forgotpassword(request):
    if request.method == 'POST':
        username_email=request.POST['username_email']
        password=request.POST['password']
        print(password)
        confirmpassword=request.POST['confirm_password']
        user_obj = UserSignup.objects.filter(Q(Username=username_email) | Q(Email=username_email)).values()
        if confirmpassword != password:
            print("password is not matching")
            messages.error(request, 'Password and Confirm Password are not matching!')
            return render(request, 'forgotpassword.html')
        else:
            print(user_obj)
            print(user_obj[0]['Username'])
            try:
                user=User.objects.get(username=user_obj[0]['Username'])
                user.set_password(password)
                print(f'{password}')
                user.save()
                print("password changed successfully")
                print(user.password) 
            except:
                messages.error(request, 'Some error occured')
            return redirect('signin')
                   
    else:
        return render(request,'forgotpassword.html')

def checkusernameemail(request):
    print("Username or Email checking ")
    print(request.POST)
    print(request.POST['username_email'])
    username_email = request.POST['username_email']
    email_availability = UserSignup.objects.filter(Q(Username=username_email) | Q(Email=username_email))
    if email_availability:
        status = 'not available'
    else:
        status = 'success'

    print(email_availability)
    print(status)
    return JsonResponse({'status': status})

def pincode(request):
    a=requests.get('https://api.postalpincode.in/pincode/'+request.POST['pin'])
    d = json.loads(a.text)
    finaldict=d[0]
    if finaldict['Status'] == 'Success':
        post = finaldict['PostOffice']
        return JsonResponse({'status': finaldict['Status'],'city':post[0]['District'],'state': post[0]['State']})

    else:

        return JsonResponse({'status': finaldict['Status']})

@login_required
def chat(request):
    u=request.user.username
    print("chatroom view")
    print(u) 
    return render(request,'chat_room.html',{'username':u})

@login_required
def personal_chat(request,other_user):
    username=request.user.username
    second_user=User.objects.get(username=other_user)
    print("persoanl chat")
    print(username)
    thread_obj=Thread.objects.get_or_create_personal_thread(request.user,second_user)
    if thread_obj != None:
        print(thread_obj.id)
        messages=Message.objects.filter(thread=thread_obj).order_by('created_at')
        print(len(messages))
        for m in messages:
            print(m.sender)
            print(m.text)
            print(m.created_at)
        
    return render(request,'chat-conversation.html',{'username':username,'other_user':other_user,'messages':messages})
