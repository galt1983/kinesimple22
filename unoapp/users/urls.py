from django.contrib import admin
from django.urls import path, include
from users import views 
#from users import views as users_views  para no mezclar vistas creo que el otro lo habia puesto así


urlpatterns = [
    path("",views.home, name="home"),
    path("signup",views.signup, name="signup"),
    path("signin",views.signin, name="signin"),
    path("signout",views.signout, name="signout"),  
]