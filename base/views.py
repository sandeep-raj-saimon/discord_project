from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *
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
    params = {}
    rooms = Room.objects.all()
    params["rooms"] = rooms
    return render (request, 'base/home.html',params)

def room(request, pk):
    room = None
    params = {}
    room = Room.objects.get(id = pk)
    params["room"] = room
    # return HttpResponse("Room Page")
    return render (request, 'base/room.html', params)

def createRoom(request):
    params = {}
    return render (request, 'base/room_form.html', params)