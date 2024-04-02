from django.contrib import admin
from django.urls import path
from .views import *

'''urlpatterns = [
    path('admin/', admin.site.urls),
]
'''
urlpatterns=[
    #path("",hello1),
    path("h/",hello,name='hello'),
    path("",newhomepage,name='newhomepage'),
    path("a/",travelpackage,name='travelpackage'),
    path("s/",printconsole,name='printconsole'),
    path("form/",print1,name='print1'),
    path("timezfnccall/",timezfnccall,name='timezfnccall'),
    path("ran/",random123,name='random123'),
    path("h1/",random1,name='random1'),
    path("context/",Randomotp,name='randomotp'),
    path("d/",getDate1,name='getDate1'),
    path("date1/",getdate,name='getdate'),
    path("l/",postgre,name='postgre'),
    path("reg/",loginfunc,name='loginfunc'),
    path("c/",piechart,name='piechart'),
    path("e/",pie_chart,name='pie_chart'),
    path("t/",carousel,name='carousel'),
    path("w/",weathercall,name='weathercall'),
    path("weather/",weatherlogic,name='weatherlogic'),
    path("login/",login,name='login'),
    path("signup/",signup,name='signup'),
    path("signup1/",signup1,name='signup1'),
    path("login1/",login1,name='login1'),
    path("logout/",logout,name='logout'),
    path("feed/",feedback,name='feedback'),
    path("contactmail/",contactmail,name='contactmail'),

]