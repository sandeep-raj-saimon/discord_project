from django.shortcuts import render, redirect
from django.http import HttpResponse
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
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    params = {}
    rooms = Room.objects.filter(topic__name__icontains = q)
    topics = Topic.objects.all()
    params["rooms"] = rooms
    params["topics"]= topics
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