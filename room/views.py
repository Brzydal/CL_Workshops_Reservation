from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from room.models import *
# Create your views here.

def all_rooms(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,'room/all_rooms.html',context)
    
class AddRoom(View):
    
    def get(self,request):
        return render(request,'room/room_form.html')
    
    def post(self,request):
        name = request.POST.get('name')
        capacity = int(request.POST.get('capacity'))
        projector = bool(request.POST.get('projector'))
        
        room = Room.objects.create(name = name, capacity = capacity, projector = projector)
         
        return redirect('/')
