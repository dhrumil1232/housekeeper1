from django.shortcuts import render, redirect,HttpResponse
from user.emailbackend import EmailBackend
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from user.models import CustomUser

def  Base(request):
    return render(request, 'base.html')
def Login(request):
    return render(request, 'login.html')
def DoLogin(request):
    if request.method == 'POST':
        user = EmailBackend.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        
        if user!=None:
            login(request, user)
            user_type= user.user_type
            if user_type=='1':
                return redirect('admin_home')
            elif user_type=='2':
                return redirect('housekeeper_home')
            elif user_type=='3':
                return redirect('customer_home')
            else:
                messages.error(request,'Email and Password are invalid!')
                return redirect('login')
        else:
            messages.error(request,'Email and Password are invalid!')
            return redirect('login')
def DoLogout(request):
    logout(request)
    return redirect('login')
@login_required(login_url='/')
def Profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    
    
    context ={
        "user":user
    }
    return render(request, 'profile.html')
@login_required(login_url='/')
def UpdateProfile(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name= request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password != '' and password != None:
                customuser.set_password(password)
            if profile_pic != '' and profile_pic != None:
                customuser.profile_pic = profile_pic
            customuser.save()
            messages.success(request, 'Profile Updated Successfully!')
            redirect('profile')
        except:
            messages.error(request, 'Something went wrong!')
    return render(request, 'profile.html')