from django.shortcuts import render,redirect
from django.http import Http404
from django.shortcuts import get_object_or_404
from . models import Tour
from . models import Reservation,Employee
from django.contrib import messages
from datetime import date
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    
    tour = Tour.objects.all()
    context = {
        'tour': tour
    }
     
         
    return render(request, 'tour/list.html', context)

def detail(request, tour_id):
    tour = Tour.objects.get(pk=tour_id) 

    context = {
        'tour': tour,
    }
    return render(request, 'tour/detail.html', context)

def search(request):
    return render(request,'tour/search.html')


def reservation(request,tour_id):
    tour = Tour.objects.get(pk = tour_id)
    context = {
        'tour' : tour,
    }
    return render(request, 'tour/reservation.html',context)  



def make_reservation(request, tour_id):
    tour = get_object_or_404(Tour, pk=tour_id)
    employee = tour.Trip_Employee

    context = {
        'tour': tour,
        'employee': employee,
    }

    if request.method == 'POST':
        reservation_note = request.POST['Reservation_Note']
        customer_id = request.POST['Customer_id']
        customer = get_object_or_404(User, pk=customer_id)
        reservation_price = tour.Trip_Price

        try:
            reservation = Reservation.objects.create(
                Reservation_Note=reservation_note,
                Reservation_Customer=customer,
                Reservation_Trip=tour,
                Reservation_Time=date.today(),
                Reservation_Price=reservation_price,
                Reservation_Employee=employee,
            )
            reservation.save()
            messages.success(request, 'Reservation created successfully!')
        except Exception as e:
            messages.error(request, f'An error occurred: {e}')

    return render(request, 'tour/reservation.html', context)

