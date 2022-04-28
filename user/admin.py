from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class UserModel(UserAdmin):
    list_display= ['username','user_type']
admin.site.register(CustomUser,UserModel)
admin.site.register(Service)
admin.site.register(Housekeeper)
admin.site.register(Customer)
admin.site.register(Housekeeper_Notification)
admin.site.register(Housekeeper_Leave)
admin.site.register(Housekeeper_Feedback)