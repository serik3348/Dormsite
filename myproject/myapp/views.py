import cx_Oracle
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from .models import *
from django.db import connection

from .forms import StudentForm, BalanceForm


# Create your views here.


def show_main(request):
    student = Dormstudents.objects.all()
    return render(request, 'main/home.html', )


def student_register(request):
    if request.method == 'POST':
     form=StudentForm(request.POST)

     if form.is_valid():
         form.save()
         form = StudentForm()

    else:
        form = StudentForm()

    return render(request, 'main/register.html', {"form": form})

def show_status(request):

    searched=request.GET.get('search')
    searched1=request.GET.get('search2')
    if not searched:
        search_query = ""
    if not searched1:
        search_query = "SEIK"
    dormstudents=Dormstudents.objects.filter(student_id=searched)
    dormrooms=Dormrooms.objects.filter(student_id=searched1)

    cursor = connection.cursor()
    busy_rooms = cursor.callfunc('room_count', cx_Oracle.NUMBER)
    getstudents_num=cursor.callfunc('getstudents_num', cx_Oracle.NUMBER)


    context={
        'dormstudents':dormstudents,
        'busy_rooms': busy_rooms,
        'dormrooms': dormrooms,
        'getstudents_num':getstudents_num
    }

    return render(request,'main/status.html',context)



def show_balance(request):
    if request.method == 'POST':
        form = BalanceForm(request.POST)

        if form.is_valid():
            form.save()
            form = BalanceForm()

    else:
        form = BalanceForm()

    return render(request, 'main/balance.html', {"form": form})

