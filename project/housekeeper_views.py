from multiprocessing import context
from django.shortcuts import render, redirect
from user.models import *
from django.contrib import messages
def Home(request):
    return render(request, 'housekeeper/home.html')
def Notification(request):
    housekeeper = Housekeeper.objects.filter(admin = request.user.id)
    for i in housekeeper:
        housekeeper_id = i.id
        notification = Housekeeper_Notification.objects.filter(housekeeper_id = housekeeper_id)
        context ={
            'notification':notification,
        }
    return render(request, 'housekeeper/notification.html',context)
def mark_as_read(request,status):
    notification = Housekeeper_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('notification')
def Apply_Leave(request):
    housekeeper = Housekeeper.objects.filter(admin = request.user.id)
    for i in housekeeper:
        housekeeper_id = i.id
        housekeeper_leave_history = Housekeeper_Leave.objects.filter(housekeeper_id = housekeeper_id)
        context = {
            'housekeeper_leave_history':housekeeper_leave_history,
        }
    
    return render(request, 'housekeeper/apply_leave.html',context)

def Save_Leave(request):
   if request.method == 'POST':
       leave_date = request.POST.get('date')
       leave_message = request.POST.get('leave_message')
       housekeeper = Housekeeper.objects.get(admin = request.user.id)
       leave = Housekeeper_Leave(
           housekeeper_id = housekeeper,
           date = leave_date,
           leave_message = leave_message,
       )
       leave.save()
       messages.success(request, 'Leave applied successfully')
       return redirect('apply_leave')
   
def Feedback(request):
    housekeeper_id = Housekeeper.objects.get(admin = request.user.id)
    feedback_history = Housekeeper_Feedback.objects.filter(housekeeper_id =housekeeper_id)
    context ={
        'feedback_history':feedback_history,
    }    
    return render(request, 'housekeeper/feedback.html',context)

def Save_Feedback(request):
    if request.method == 'POST':
        housekeeper_feedback = request.POST.get('housekeeper_feedback')
        housekeeper = Housekeeper.objects.get(admin = request.user.id)
        feedback_data = Housekeeper_Feedback(
            housekeeper_id = housekeeper,
            housekeeper_feedback = housekeeper_feedback,
            housekeeper_feedback_reply = "",
        )
        feedback_data.save()
        messages.success(request, 'Feedback submitted successfully')
        return redirect('feedback')
