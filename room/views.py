from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from room.models import *
# Create your views here.
class AddRoom(View):
    
    def get(self,request):
        
        return render(request,'room/room_form.html')
    
    def post(self,request):
#         form_name = request.POST.get('name')
#         form_surname = request.POST.get('surname')
#         form_city = request.POST.get('city')
#         form_street = request.POST.get('street')
#         form_house_number = request.POST.get('house_number')
#         form_email = request.POST.get('email')
#         form_telephone = request.POST.get('telephone')
#         form_type = request.POST.get('type')
#         form_description = request.POST.get('description')
#         
#         address = Address.objects.create(city=form_city, street=form_street, house_number=form_house_number)
#         person = Person.objects.create(name=form_name,surname=form_surname,description=form_description,address=address)
#         email = Email.objects.create(email=form_email,person=person)
#         telephone = Telephone.objects.create(tel_number=form_telephone,type=form_type,person=person)         
#     
#         return redirect('/person_details/{}'.format(person.id))
        return HttpResponse('boom!')