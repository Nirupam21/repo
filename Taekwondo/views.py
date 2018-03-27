from django.shortcuts import render
from Taekwondo.models import Players
from django.http import HttpResponseRedirect
from Taekwondo.forms import PlayerForm
from django.contrib import auth
from django.contrib.auth.models import User

def Home(request):
    return render(request,'base.html',{})

def about(request):
    return render(request, 'about.html', {})

def index(request):
    allrows=Players.objects.all()
    return render(request,'player.html', {'allrows': allrows})

def delete(request, id):
    record = Players.objects.get(id=id)
    record.delete()
    return render(request,'delete.html', {'record': record})

def del1(request):
   if request.method == "POST":
        try:
           a = request.POST.get("delete", '')
           record = Players.objects.filter(name=a)
           return render(request, 'searchdel.html', {'record': record})
        except:
            return render(request, 'del.html', {'errMsg': 'Player Not Found!!!!!!'})
   else:
        return render(request, 'del.html', {})

def addItem(request):
    if request.method == "POST":
        i = Players()
        i.name = request.POST.get('name', '')
        i.gender = request.POST.get('gender', '')
        i.age = request.POST.get('age', '')
        i.agegroup = request.POST.get('agegroup', '')
        i.weight = request.POST.get('weight', '')
        i.weightcategory = request.POST.get('weightcategory', '')
        i.PlayingFor = request.POST.get('PlayingFor', '')
        i.state = request.POST.get('state', '')
        i.country = request.POST.get('country', '')
        i.save()
        return render(request, 'itemadded.html', {})
    else:
        pf = PlayerForm
        return render(request, 'add.html', {'form': pf})

def findproduct(request):
    if request.method == "POST":
        try:
            i = request.POST.get("titletext", '')
            record = Players.objects.get(name=i)
            return render(request, 'searchpro.html', {'record': record})
        except:
            return render(request, 'findproduct.html', {'errMsg': 'Player Not Found!!!!!!'})
    else:
        return render(request, 'findproduct.html', {})

def search(request):
    if request.method == "POST":
        try:
            i = request.POST.get("age", '')
            j = request.POST.get("w", '')
            k = request.POST.get("gen", '')
            record = Players.objects.filter(agegroup=i).filter(gender=k).filter(weightcategory=j)
            return render(request, 'search.html', {'record': record})
        except:
            return render(request, 'find.html', {'errMsg': 'Record Not Found!!!'})
    else:
        return render(request, 'find.html', {})

def tournament(request):
    if request.method == "POST":
        try:
            i= request.POST.get("age", '')
            j = request.POST.get("gen", '')
            k = request.POST.get("w", '')
            record = Players.objects.filter(agegroup=i).filter(gender=j).filter(weightcategory=k)
            count = record.count()
            if count == 2 or count == 4 or count == 8 or count == 16 or count == 32 or count == 64 or count == 128:
                return render(request, 'fixture1.html', {'record': record})
            elif count > 0:
                return render(request, 'fixture2.html', {'record': record})
            else:
                return render(request, 'tour.html', {'errMsg': 'Record Not Found!!!'})
        except:
            return render(request, 'tour.html', {'errMsg': 'Record Not Found!!!'})
    else:
        return render(request, 'tour.html', {})

def login(request):
    return render(request,'login.html',{})

def auth_view(request):
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return render(request,'about.html/',{'user':user})
    else:
        return HttpResponseRedirect('/invalid.html/')


def invalid(request):
    return render(request,'invalid.html',{})

def logout(request):
    auth.logout(request)
    return render(request,'logout.html',{})