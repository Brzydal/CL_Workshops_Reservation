"""Reservation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from room.views import all_rooms,delete_room, room_details,all_reservations,delete_reservation
from room.views import AddRoom, ModifyRoom, AddReservation, search
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^room/new$', AddRoom.as_view()),
    url(r'^room/modify/(?P<room_id>\d+)$', ModifyRoom.as_view()),
    url(r'^room/delete/(?P<room_id>\d+)$', delete_room),
    url(r'^room/(?P<room_id>\d+)$', room_details),
    url(r'^reservation/new/(?P<room_id>\d+)$', AddReservation.as_view()),
    url(r'^reservation/new$', AddReservation.as_view()),
    url(r'^reservation/all$', all_reservations),
    url(r'^reservation/delete/(?P<reservation_id>\d+)$', delete_reservation),
    url(r'^search/', search),
    url(r'^$', all_rooms),
]
