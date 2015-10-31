from django.contrib import admin
from gwalior.models import Complaints
from django.contrib.auth.models import User

# Register your models here.

class ComplaintAdmin(admin.ModelAdmin):
	list_display = ('type_of_complaint', 'complaint_title', 'solved', 'preference')

# class UserProfileAdmin(admin.ModelAdmin):
# 	list_display = ('User.username', 'User.email')

admin.site.register(Complaints, ComplaintAdmin)
#admin.site.register(UserProfile)