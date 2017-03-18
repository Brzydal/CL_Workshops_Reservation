from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from datetime import datetime
from room.models import *
    
class AddRoom(View):
    
    def get(self,request):
        room = Room()
        return render(request,'room/room_form.html')
    
    def post(self,request):
        name = request.POST.get('name')
        capacity = int(request.POST.get('capacity'))
        projector = bool(request.POST.get('projector'))
        room = Room.objects.create(name = name, capacity = capacity, projector = projector)
        return redirect('/')

class ModifyRoom(View):
    
    def get(self,request,room_id):
        room = Room.objects.get(pk=room_id)
        context = {'room':room}
        return render(request,'room/room_form.html',context)
    
    def post(self,request,room_id):
        room = Room.objects.get(pk=room_id)
        room.name = request.POST.get('name')
        room.capacity = int(request.POST.get('capacity'))
        room.projector = bool(request.POST.get('projector'))
        room.save()
        return redirect('/')

def all_rooms(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,'room/all_rooms.html',context)

def delete_room(request,room_id):
    room = Room.objects.get(pk=room_id)
    room.delete()
    return redirect('/')

def room_details(request,room_id):
    room = Room.objects.get(pk=room_id)
    context = {'room':room}
    return render(request,'room/room_details.html',context)

class AddReservation(View):
    
    def get(self,request):
        rooms = Room.objects.all()
        context = {'rooms':rooms}
        reservation = Reservation()
        return render(request,'room/reservation_form.html',context)
    
    def post(self,request):
        room_id = request.POST.get('room')
        date = datetime.date(datetime.strptime(request.POST.get('date'),'%Y-%m-%d'))
        comment = request.POST.get('comment')
        room = Room.objects.get(pk=room_id)
        reservation = Reservation.objects.create(room_id=room, date=date,comment=comment)
        return redirect('/')
    
