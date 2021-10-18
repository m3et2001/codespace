from . import views
from django.urls import path,include


urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('signout',views.signout,name='signout'),
    path('',views.signin,name='signin'),
    path('choose-user',views.chooseuser,name='chooseuser'),
    path('check-email',views.check_email,name='checkemail'),
    path('check-username',views.check_username,name='checkusername'),
    path('chat',views.chat,name='chat'),
    path('personal-chat/<slug:other_user>',views.personal_chat,name='personal-chat'),
    path('chat-option',views.chatoption,name="chatoption"),
    path('registeruser',views.googleregister,name='googleregister'),
    path('email-verification/<slug:token>',views.emailverification,name="emailverification"),
    path('forgot-password',views.forgotpassword,name='forgotpassword'),
    path('check-username-email',views.checkusernameemail,name='checkusernameemail'),
    path('pincode',views.pincode,name='pincode')
    #<slug:other_user>
    


]
