from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.index, name = "index"),
    path('home', views.home, name = "home"),
    path('profile', views.profile, name = "profile"),
    path('postDelete/<int:id>/', views.deletePost, name = "deletePost"),

]
