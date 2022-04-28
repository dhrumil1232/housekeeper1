from email import message
from multiprocessing import context
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user.models import *








@login_required(login_url='/')
def Home(request):
    customer_count = Customer.objects.all().count()
    housekeeper_count = Housekeeper.objects.all().count()
    service_count = Service.objects.all().count
      
    context ={
        'customer_count':customer_count,
        'housekeeper_count':housekeeper_count,
        'service_count':service_count,
        
    }
    return render(request, 'Admin/home.html',context)
@login_required(login_url='/')
def AddHousekeeper(request):
    service = Service.objects.all()
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password= request.POST.get('password')
        service_id = request.POST.get('service_id')
        state= request.POST.get('state')
        city= request.POST.get('city')
        area= request.POST.get('area')
        address= request.POST.get('address')
        experience= request.POST.get('experience')
        id_proof = request.FILES.get('id_proof')
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email already exists')
            return redirect('add_housekeeper')
        
        
        
        
        
        
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username already exists')
            return redirect('add_housekeeper')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=2,
            )
            user.set_password(password)
            user.save() 
            service = Service.objects.get(id=service_id)
            housekeeper = Housekeeper(
                admin = user,
                address=address,
                state = state,
                city = city,
                area = area,
                service_id = service,
                id_proof = id_proof,
                experience=experience,
            )
            housekeeper.save()
            messages.success(request, 'Housekeeper added successfully')
            return redirect('add_housekeeper')
            
            
        
    context = {
        'service':service
        }
    return render(request, 'Admin/add_housekeeper.html' ,context)
@login_required(login_url='/')
def ViewHousekeeper(request):
    housekeeper = Housekeeper.objects.all()
    context = {
        'housekeeper':housekeeper
    }
    return render(request, 'Admin/view_housekeeper.html',context)
def EditHousekeeper(request,id):
    housekeeper = Housekeeper.objects.filter(id=id)
    service = Service.objects.all()
    context ={
        'housekeeper':housekeeper,
        'service':service,
    }
    return render(request, 'Admin/edit_housekeeper.html',context)
@login_required(login_url='/')
def UpdateHousekeeper(request):
    if request.method =="POST":
        housekeeper_id = request.POST.get('housekeeper_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password= request.POST.get('password')
        service_id = request.POST.get('service_id')
        state= request.POST.get('state')
        city= request.POST.get('city')
        area= request.POST.get('area')
        address= request.POST.get('address')
        experience= request.POST.get('experience')
        id_proof = request.FILES.get('id_proof')    
        user = CustomUser.objects.get(id=housekeeper_id)
        
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        if password != '' and password != None:
            user.set_password(password)
        if profile_pic != '' and profile_pic != None:
            user.profile_pic = profile_pic
        user.save()
        
    housekeeper = Housekeeper.objects.get(admin=housekeeper_id)
    housekeeper.address = address
    housekeeper.state = state
    housekeeper.city = city
    housekeeper.area = area
    service = Service.objects.get(id = service_id)
    housekeeper.service_id = service 
    if id_proof != '' and id_proof != None:
            housekeeper.id_proof = id_proof
    housekeeper.experience = experience
    housekeeper.save()
    messages.success(request, 'Housekeeper updated successfully')
    return redirect('view_housekeeper')

@login_required(login_url='/')
def DeleteHousekeeper(request,admin):
    housekeeper = CustomUser.objects.get(id=admin)
    housekeeper.delete()
    messages.success(request, 'Housekeeper deleted successfully')
    return redirect('view_housekeeper')

@login_required(login_url='/')
def AddService(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        category = request.POST.get('category')
        image= request.FILES.get('image')
        service = Service(
            name=name,
            price =price,
            description=description,
            image = image,
            category = category
        )
        service.save()
        messages.success(request, 'Service added successfully')
        return redirect('add_service')
    return render(request, 'Admin/add_service.html')
@login_required(login_url='/')
def ViewService(request):
    service = Service.objects.all()
    context = {
        'service':service
    }
    return render(request, 'Admin/view_service.html',context)
@login_required(login_url='/')
def EditService(request,id):
    service = Service.objects.filter(id=id)
    context ={
        'service':service,
    }
    return render(request, 'Admin/edit_service.html',context)
@login_required(login_url='/')
def UpdateService(request):
    if request.method =="POST":
        service_id = request.POST.get('service_id')
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image= request.FILES.get('image')
        category = request.POST.get('category')
        
        service = Service.objects.get(id=service_id)
        if image != '' and image != None:
            service.image = image

        service.name=name
        service.price =price
        service.description=description
        service.category = category
    
        service.save()
        messages.success(request, 'Service updated successfully')
        return redirect('view_service')
@login_required(login_url='/')    
def DeleteService (request,id):
    service = Service.objects.get(id=id)
    service.delete()
    messages.success(request, 'Service deleted successfully')
    return redirect('view_service')

#Customer Section
@login_required(login_url='/')
def AddCustomer(request):
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
            messages.success(request, 'Customer added successfully')
            return redirect('add_customer')
            
            
        
    return render(request, 'Admin/add_customer.html')
@login_required(login_url='/')
def ViewCustomer(request):
    customer = Customer.objects.all()
    context = {
        'customer':customer
    }
    return render(request, 'Admin/view_customer.html',context)
@login_required(login_url='/')
def EditCustomer(request,id):
    customer = Customer.objects.get(id=id)
    context ={
        'customer':customer,
    }
    return render(request, 'Admin/edit_customer.html',context)
@login_required(login_url='/')
def UpdateCustomer(request):
    if request.method =="POST":
        customer_id = request.POST.get('customer_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password= request.POST.get('password')
        state= request.POST.get('state')
        city= request.POST.get('city')
        area= request.POST.get('area')
        address= request.POST.get('address')
        user = CustomUser.objects.get(id=customer_id)
        
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        if password != '' and password != None:
            user.set_password(password)
        if profile_pic != '' and profile_pic != None:
            user.profile_pic = profile_pic
        user.save()
        
    customer = Customer.objects.get(admin=customer_id)
    customer.address = address
    customer.state = state
    customer.city = city
    customer.area = area
    customer.save()
    messages.success(request, 'Customer updated successfully')
    return redirect('view_customer')
@login_required(login_url='/')
def DeleteCustomer(request,admin):
    customer = CustomUser.objects.get(id = admin)
    customer.delete()
    messages.success(request, 'Customer deleted successfully')
    return redirect('view_customer')
@login_required(login_url='/')
def Housekeeper_Send_Notification(request):
    see_notification = Housekeeper_Notification.objects.all().order_by('-id')[0:5]
    housekeeper = Housekeeper.objects.all()
    context ={
        'housekeeper':housekeeper,
        'see_notification':see_notification
    }
    return render(request,'Admin/housekeeper_notification.html',context)
@login_required(login_url='/')
def Save_Notification(request):
    if request.method == 'POST':
        housekeeper_id = request.POST.get('housekeeper_id')
        
        message= request.POST.get('message')
        housekeeper = Housekeeper.objects.get(admin = housekeeper_id)
        notification = Housekeeper_Notification(
            housekeeper_id = housekeeper,
            message = message,
        )
        notification.save()
        messages.success(request, 'Notification sent successfully')
        return redirect('housekeeper_send_notification')
@login_required(login_url='/')
def Leave_View(request):
    leave = Housekeeper_Leave.objects.all()
    context ={
        'leave':leave
    }
    return render(request,'Admin/leave_view.html',context)
@login_required(login_url='/')
def Approve_Leave(request,id):
    leave = Housekeeper_Leave.objects.get(id = id)
    leave.status = 1
    leave.save()
    messages.success(request, 'Leave approved successfully')
    return redirect('leave_view')
@login_required(login_url='/')
def Reject_Leave(request,id):
    leave = Housekeeper_Leave.objects.get(id = id)
    leave.status = 2
    leave.save()
    messages.error(request, 'Leave rejected successfully')
    return redirect('leave_view')
@login_required(login_url='/')
def Feedback_Housekeeper_Reply(request):
    feedback = Housekeeper_Feedback.objects.all()
    context ={
        'feedback':feedback
    }
    
    return render(request,'Admin/feedback_housekeeper.html',context)
def Feedback_Housekeeper_Reply_Save(request):
    if request.method == 'POST':
        feedback_id = request.POST.get('feedback_id')
        housekeeper_feedback_reply = request.POST.get('housekeeper_feedback_reply')
        feedback = Housekeeper_Feedback.objects.get(id = feedback_id)
        feedback.housekeeper_feedback_reply = housekeeper_feedback_reply
        feedback.save()
        messages.success(request, 'Reply sent successfully')
        return redirect('feedback_housekeeper_reply')