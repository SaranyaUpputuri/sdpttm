import random
import string

from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse

from .forms import *


# Create your views here.

def hello1(request):
    return HttpResponse("<center><font color=blue>Welcome to TTM Homepage</center>")
def hello(request):
    return render(request,'homepage.html')

def newhomepage(request):
    return render(request,'newhomepage.html')

def travelpackage(request):
    return render(request,'travelpackage.html')

def print1(request):
    return render(request,'printconsole.html')

def printconsole(request):
    if request.method=="POST":
        user_input=request.POST['user_input']
        print(f'user_input:{user_input}')
    #return HttpResponse('Form Submitted Successfully')
    a1={'user_input':user_input}
    return render(request,'printconsole.html',a1)

def random123(request):
    import string
    import random
    ran1 = ''.join(random.sample(string.digits, k=6))
    print(ran1)
    a2={'ran1':ran1}
    return render(request,'random123.html',a2)

def random1(request):
    return render(request,"randomotp.html")


def Randomotp(request):
    if request.method == 'POST':
        input1 = request.POST['input1']
        input2 = int(input1)
        result_str=''.join(random.sample(string.digits, input2))
        print(result_str)
        context = {'result_str':result_str}
    return render(request,"randomotp.html",context)


def getDate1(request):
    return render(request,'getdate.html')

import datetime
from django.shortcuts import render
def getdate(request):
    if request.method == 'POST':
        form = Integerdateform(request.POST)
        if form.is_valid():
            integer_value = form.cleaned_data['integer_value']
            date_value = form.cleaned_data['date_value']
            updated_date = date_value + datetime.timedelta(days=integer_value)
            return render(request,'getdate.html',{'updated_date':updated_date})
        else:
            form = Integerdateform()
        return render(request,'getdate.html',{'form':form})

def timezfnccall(request):
    return render(request,'pytzex.html')

#def tzfunclogic(request):
 #   return

def postgre(request):
     return render(request,'login.html')
from.models import *
from django.shortcuts import render,redirect
def loginfunc(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password  = request.POST.get('password')
        phonenumber = request.POST.get('phonenumber')
        if Register.objects.filter(email=email).exists():
            msg1 = "Email already exists.Choose different one."
            return render(request,'login.html',{'msg1':msg1})
        Register.objects.create(name=name, email=email, password=password, phonenumber=phonenumber)
        return redirect('newhomepage')
    return render(request,'login.html')

def piechart(request):
    return render(request,'chartform.html')

import matplotlib.pyplot as plt
import numpy as np

def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1={'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'chartform.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'chartform.html', {'form': form})

def carousel(request):
    return render (request,'carousel.html')

import requests
def weathercall(request):
    return render(request,'weather.html')

def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = '64ce8cf4fd1337dcb78bf1ebbc0c52c7'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1= round(temperature - 273.15,2)
            return render(request, 'weather.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weather.html', {'error_message': error_message})

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')
def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return render(request,'newhomepage.html')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def signup1(request):
    if request.method == "POST":
        username=request.POST['username']
        pass1=request.POST['password']
        pass2=request.POST['password1']
        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'OOPS! Username already taken')
                return render(request,'signup.html')
            else:
                user=User.objects.create_user(username=username,password=pass1)
                user.save()
                messages.info(request,'Account created successfully!')
                return render(request,'login.html')
        else:
            messages.info(request,'Password do not match')
            return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return render(request,'newhomepage.html')

def feedback(request):
    return render(request,'Contact.html')

def contactmail(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        comment = request.POST['comment']
        tosend = comment + '--------------This is just an example'
        data = contactus(firstname=firstname, lastname=lastname, email=email, comment=comment)
        data.save()
        return HttpResponse("Contact information saved successfully")


        
