from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import UserSignup,Profile,Message,Thread

@admin.register(UserSignup)
class UserSignupAdmin(admin.ModelAdmin):
    list_display=('Username','Firstname','Lastname')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','token','verify')

@admin.register(Thread)
class ThreadAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('thread_type',)

@admin.register(Message)
class MessageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('thread','sender','text')