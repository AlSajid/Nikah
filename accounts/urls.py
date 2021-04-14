from django.urls import path
from . import views
urlpatterns = [
    
    path('register', views.createAccount, name = "createAccount"),
    path('login', views.log_in, name = "login"),
    path('logout', views.log_out, name = "logout"),
    path('editProfile', views.editProfile, name = "editProfile"),
    

]
