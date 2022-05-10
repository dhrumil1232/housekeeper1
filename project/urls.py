
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from user.models import Housekeeper
from . import customer_views, views,admin_views,housekeeper_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.Base, name='base'),
    
    
    #Login Path
    path('login/', views.Login, name='login'),
    path('dologin/', views.DoLogin, name='dologin'),
    path('dologout/', views.DoLogout, name='logout'),
    
    #Profile update
    path('profile/', views.Profile, name='profile'),
    path('profile/update/', views.UpdateProfile, name='updateprofile'),
    
    
    
    # Admin Panel Path 
    path('Admin/Home', admin_views.Home, name='admin_home'),
    path('Admin/Housekeeper/Add', admin_views.AddHousekeeper, name='add_housekeeper'),
    path('Admin/Housekeeper/View', admin_views.ViewHousekeeper, name='view_housekeeper'),
    path('Admin/Housekeeper/Edit/<str:id>', admin_views.EditHousekeeper, name='edit_housekeeper'),
    path('Admin/Housekeeper/Update/',admin_views.UpdateHousekeeper, name='update_housekeeper'),
    path('Admin/Housekeeper/Delete/<str:admin>', admin_views.DeleteHousekeeper, name='delete_housekeeper'),

    
    # Customer Panel Path
    path('Admin/Customer/Add', admin_views.AddCustomer, name='add_customer'),
    path('Admin/Customer/View', admin_views.ViewCustomer, name='view_customer'),
    path('Admin/Customer/Edit/<str:id>', admin_views.EditCustomer, name='edit_customer'),
    path('Admin/Customer/Update/',admin_views.UpdateCustomer, name='update_customer'),
    path('Admin/Customer/Delete/<str:admin>', admin_views.DeleteCustomer, name='delete_customer'),
    
    #service path
    path('Admin/Service/Add', admin_views.AddService, name='add_service'),
    path('Admin/Service/View', admin_views.ViewService, name='view_service'),
    path('Admin/Service/Edit/<str:id>', admin_views.EditService, name='edit_service'),
    path('Admin/Service/Update/',admin_views.UpdateService, name='update_service'),
    path('Admin/Service/Delete/<str:id>', admin_views.DeleteService, name='delete_service'),
    path('Admin/Housekeeper/Send_notification',admin_views.Housekeeper_Send_Notification,name='housekeeper_send_notification'),
    path('Admin/Housekeeper/Save_Notification',admin_views.Save_Notification,name ='housekeeper_save_notification'),
    path('Admin/Housekeeper/Leave_view',admin_views.Leave_View,name='leave_view'),
    path('Admin/Housekeeper/Approve_leave,<str:id>',admin_views.Approve_Leave,name='approve_leave'),
    path('Admin/Housekeeper/Reject_leave,<str:id>',admin_views.Reject_Leave,name='reject_leave'),
    path('Admin/Housekeeper/Feedback',admin_views.Feedback_Housekeeper_Reply,name='feedback_housekeeper_reply'),
    path('Admin/Housekeeper/Feedback/Save',admin_views.Feedback_Housekeeper_Reply_Save,name='feedback_housekeeper_reply_save'),
    path('Admin/Customer/Feedback',admin_views.Feedback_Customer_Reply,name='feedback_customer_reply'),
    path('Admin/Customer/Feedback/Save',admin_views.Feedback_Customer_Reply_Save,name='feedback_customer_reply_save'),
    path('Admin/Housekeeper/Booking_view',admin_views.Booking_View,name='booking_view'),   
    path('Admin/Housekeeper/Approve_booking,<str:id>',admin_views.Approve_Booking,name='approve_booking'),
    path('Admin/Housekeeper/Reject_booking,<str:id>',admin_views.Reject_Booking,name='reject_booking'),
    # this is Housekeeper Url
    path('Housekeeper/Home', housekeeper_views.Home, name='housekeeper_home'),    
    path('Housekeeper/Notification', housekeeper_views.Notification, name='notification'),
    path('Housekeeper/mark_as_read/<str:status>', housekeeper_views.mark_as_read, name='mark_as_read'),    
    path('Housekeeper/Apply_leave', housekeeper_views.Apply_Leave, name='apply_leave'),
    path('Housekeeper/Save_Leave', housekeeper_views.Save_Leave, name='save_leave'),
    path('Housekeeper/Feedback', housekeeper_views.Feedback, name='feedback'),
    path('Housekeeper/Save_Feedback', housekeeper_views.Save_Feedback, name='save_feedback'),
    # this is customer panel url
    path('', customer_views.Home, name='customer_home'),
    path('Customer/Signup', customer_views.SignupCustomer, name='customer_signup'),
    path('Customer/Save_Signup', customer_views.Save_Signup, name='customer_save_signup'),
    path('Customer/Booking', customer_views.Service_Booking, name='customer_booking'),
    path('Customer/Service', customer_views.Service_get, name='customer_service'),
    path('Customer/Save_booking', customer_views.Save_booking, name='save_booking'),
    path('Customer/AboutUs', customer_views.AboutUs, name='customer_aboutus'),
    path('Customer/ContactUs', customer_views.ContactUs, name='customer_contactus'),
    path('Customer/Feedback', customer_views.Customer_Feedback1, name='customer_feedback'),
    path('Customer/Save_Feedback', customer_views.Save_Feedback_Customer, name='save_customer_feedback'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
