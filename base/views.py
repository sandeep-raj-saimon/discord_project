from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from .models import *
from .forms import *
# rooms = [
#     {
#         'id':1,
#         'name':'Lets learn Python'
#     },
#     {
#         'id':2,
#         'name':'Lets learn JS'
#     },
#     {
#         'id':3,
#         'name':'Lets learn Ruby'
#     }
# ]

def loginRegister(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'User does not exist')
        
        user = authenticate(request, username = username, password = password)
        if user != None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password does not exist')
    params = {}
    return render(request, 'base/login_register.html', params)

def logoutUser(request):
    logout(request)
    return redirect('home')

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    params = {}
    rooms = Room.objects.filter(
        Q(topic__name__icontains = q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )
    rooms_count = rooms.count()
    topics = Topic.objects.all()
    params["rooms"] = rooms 
    params["topics"]= topics
    params["rooms_count"] = rooms_count
    return render (request, 'base/home.html',params)

def room(request, pk):
    room = None
    params = {}
    room = Room.objects.get(id = pk)
    params["room"] = room
    # return HttpResponse("Room Page")
    return render (request, 'base/room.html', params)

def createRoom(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    params = {'form': form}
    return render (request, 'base/room_form.html', params)

def updateRoom(request, pk):
    room = Room.objects.get(id= int(pk))
    form = RoomForm(instance = room)
    if request.method == "POST":
        form = RoomForm(request.POST, instance = room)
        if form.is_valid():
            form.save()
            return redirect('home')
    params = {'form': form}
    return render (request, 'base/room_form.html', params)

def deleteRoom(request, pk):
    room = Room.objects.get(id = int(pk))
    if request.method == "POST":
        room.delete()
        return redirect('home')
         
    params = {'room': room}
    return render(request, 'base/delete.html', params)