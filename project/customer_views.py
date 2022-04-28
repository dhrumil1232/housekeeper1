from django.shortcuts import render, redirect
from email import message
from multiprocessing import context
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user.models import *

def Home(request):
    return render(request, 'Customer/index.html')
def SignupCustomer(request):
    if request.method == 'POST':
        customer = request.POST.get('customer_id')
        first_name = request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password= request.POST.get('password')
        profile_pic = request.FILES.get('profile_pic')
        state= request.POST.get('state')
        city= request.POST.get('city')
        area= request.POST.get('area')
        address= request.POST.get('address')
        
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email already exists')
            return redirect('add_customer')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username already exists')
            return redirect('add_customer')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=3,
            )
            user.set_password(password)
            user.save() 
            
            customer = Customer(
                admin=user,
                state=state,
                city=city,
                area=area,
                address=address,
            )
            customer.save()      
            messages.success(request, 'YOUR REGISTRATION IS SUCCESSFUL')
            return redirect('customer_signup')
            
            
        
    return render(request, 'Customer/signup_customer.html')

    