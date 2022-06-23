from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Plant, Task, GreenUser, Plant_species
from .forms import PlantForm, TaskForm
import requests

def plant(request, plant_id):
    plant = Plant.objects.get(pk=plant_id)
    task_list = Task.objects.all()
    chuck = requests.get('https://api.chucknorris.io/jokes/random')
    chuck = chuck.json()
    cat = requests.get('https://excuser.herokuapp.com/v1/excuse')
    cat = cat.json()


    return render(request, 'green/plant.html',
                  {
                      'plant': plant,
                      'task_list': task_list,
                      'chuck':chuck,
                      'cat':cat,
                  })

def plant_list(request):
    plant_list = Plant.objects.all()


    return render(request, 'green/plant_list.html',
                  {
                      'plant_list':plant_list,
                   })



def add_task(request):
    submitted = False
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_task?submitted=True')
    else:
        form = TaskForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'green/add_task.html',
                  {
                      'form':form,
                      'submitted':submitted,
                  })

def add_plant(request):
    submitted = False
    if request.method == "POST":
        form = PlantForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_plant?submitted=True')
    else:
        form = PlantForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'green/add_plant.html',
                  {
                      'form':form,
                      'submitted':submitted,
                  })

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    month = month.capitalize()
    #conwert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number=int(month_number)

    #create calendar
    cal = HTMLCalendar().formatmonth(year,month_number)

    #get current year
    now = datetime.now()
    current_year = now.year
    current_month = now.month
    current_day = now.day

    # get current time
    time= now.strftime('%H:%M')

    #tasks
    task_list = Task.objects.all()
    (Task.task_date == current_month)

    return render(request,'green/home.html', {
        "year":year,
        "month":month,
        "month_number":month_number,
        "cal":cal,
        "current_year":current_year,
        "time":time,
        "current_month":current_month,
        "current_day":current_day,
        "task_list":task_list,
        "now":now,
    })



