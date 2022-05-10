from django.shortcuts import render, redirect
from email import message
from multiprocessing import context
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user.models import *

def Home(request):
    customer_count = Customer.objects.all().count()
    housekeeper_count = Housekeeper.objects.all().count()
    service_count = Service.objects.all().count
    housekeeper = Housekeeper.objects.all()
    context ={
        'customer_count':customer_count,
        'housekeeper_count':housekeeper_count,
        'service_count':service_count,
        'housekeeper':housekeeper
    }
    return render(request, 'Customer/index.html',context)
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

def Save_Signup(request):
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


def Service_get(request):
    service = Service.objects.all()
    context = {
        'service':service
    }
    return render(request, 'Customer/service.html',context)
def Service_Booking(request):
    service = Service.objects.all()
    customer = Customer.objects.filter(admin = request.user.id)
    context1 = {
        'service':service,
        'customer':customer
        } 
    return render(request, 'Customer/booking.html',context1,)

def Save_booking(request):
    service = Service.objects.all()
    if request.method == 'POST':
       booking_name = request.POST.get('booking_name')
       booking_contact = request.POST.get('booking_contact')
       booking_date = request.POST.get('booking_date')
       booking_days = request.POST.get('booking_days')
       booking_hours = request.POST.get('booking_hours')
       booking_address = request.POST.get('booking_address')
       service_id = request.POST.get('service_id')
       customer = Customer.objects.get(admin = request.user.id)
       service = Service.objects.get(id=service_id)
       booking = Book_Services(
              booking_name=booking_name,
              booking_contact=booking_contact,
              booking_date=booking_date,
              booking_days=booking_days,
              booking_hours=booking_hours,
              booking_address=booking_address,
              customer_id = customer,
              service_id =service,
              
       )
       booking.save()
       
       messages.success(request, 'YOUR BOOKING IS SUCCESSFUL')
       return redirect('customer_service')
def AboutUs(request):
    customer_count = Customer.objects.all().count()
    housekeeper_count = Housekeeper.objects.all().count()
    service_count = Service.objects.all().count
    context ={
        'customer_count':customer_count,
        'housekeeper_count':housekeeper_count,
        'service_count':service_count,
    }
    return render(request, 'Customer/about.html',context)
def ContactUs(request):
    return render(request, 'Customer/contact.html')
def Customer_Feedback1(request):
    customer_id = Customer.objects.get(admin = request.user.id)
    feedback_customer_history = Customer_Feedback.objects.filter(customer_id=customer_id)
    context ={
        'feedback_customer_history':feedback_customer_history,
    }    
    return render(request, 'customer/feedback.html',context)

def Save_Feedback_Customer(request):
    if request.method == 'POST':
        customer_feedback = request.POST.get('customer_feedback')
        customer = Customer.objects.get(admin = request.user.id)
        feedback_data_customer = Customer_Feedback(
            customer_id = customer,
            customer_feedback = customer_feedback,
            customer_feedback_reply = "",
        )
        feedback_data_customer.save()
        messages.success(request, 'Feedback submitted successfully')
        return redirect('customer_feedback')
