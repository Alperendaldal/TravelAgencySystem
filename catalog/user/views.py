from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.http import Http404
from django.contrib import auth
from django.contrib import messages
from Tour.models import Tour,Reservation
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from Tour.models import Payment 
from Tour.models import TravelHistory
import datetime
from . models import Customer_Info 


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')  
        password = request.POST.get('password')

        User = auth.authenticate(username=username, password=password)
        if User is not None:
            auth.login(request, User)
            messages.add_message(request, messages.SUCCESS, 'Oturum Açıldı')  
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, 'Hatalı kullanıcı adı ya da parola')
            return redirect('login')
    else:
        return render(request, 'user/login.html')



def logout(request):
    if request.method ==  'POST':
            auth.logout(request)
            messages.add_message(request,messages.SUCCESS,'Oturumunuz sonlandırıldı.')
            return redirect('index')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        if password == repassword:
            if User.objects.filter(username = username).exists():
                messages.add_message(request,messages.WARNING,'Kullanıcı adı zaten alınmış')
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.add_message(request, messages.WARNING,'Bu e posta adresi zaten kullanılıyor')
                    return redirect('register')
                else:
                    customer = User.objects.create_user(username=username, password=password, email=email,first_name=first_name,last_name=last_name)
                    customer.save
                    Customer_Info.objects.create(user=customer)
                    print('kullanıcı oluşturuldu')
                    
                    user = auth.authenticate(username=username, password=password)
                    auth.login(request,user)
                    redirect('user/customer_info_update')

        else: 
            messages.add_message(request, messages.WARNING,'Şifreler eşleşmiyor')
            return redirect('register')
        
    return render(request,'user/register.html')




    


def payment(request):

    reservation = Reservation.objects.filter(Reservation_Customer=request.user)
    tour = Tour.objects.all()
    context = {
        'reservation': reservation,
        'tour': tour,
    }
    return render(request, 'user/payment.html', context)
   

def make_payment(request):
    if request.method == 'POST':
   
        reservation_id = request.POST.get('reservation_id')
        
        reservation = get_object_or_404(Reservation, pk=reservation_id)
        payment_amount = reservation.Reservation_Price
        messages.success(request, 'Payment complete. Reservation is successful')



        payment = Payment.objects.create(
            Payment_ReservationID=reservation,
            Payment_Total= payment_amount
        )


        reservation.Reservation_Confirmation = True
        reservation.save()
        payment.save()


        travel_history = TravelHistory.objects.create(
        Travel_History_customer=reservation.Reservation_Customer,
        Travel_History_Trip=reservation.Reservation_Trip,
        Travel_History_Reservation=reservation,
        Travel_History_Created_Date=datetime.datetime.now()
        )
        travel_history.save()


        return redirect('payment')

    else:

        return redirect('payment')
 


def travel_history(request):

    current_user = request.user

    travel_history = TravelHistory.objects.filter(Travel_History_customer=current_user)

    context = {
        'travel_history': travel_history
    }

    return render(request, 'user/travel_history',context)
     

def customer_info_update(request):

  customer_info = None
  if request.method == 'POST':

    tel_no = request.POST['tel_no']
    emergency_number = request.POST['emergency_number']
    birthday = request.POST['birthday']
    gender = request.POST['gender']


    customer_info, created = Customer_Info.objects.get_or_create(user=request.user)

    customer_info.Tel_No = tel_no
    customer_info.Emergency_Number = emergency_number
    customer_info.Birthday = birthday
    customer_info.Gender = gender
    customer_info.save()

    messages.success(request, "Customer information updated successfully!")
    return redirect('travel_history')
  else:
    customer_info, created = Customer_Info.objects.get_or_create(user=request.user)

  form = {
    'tel_no': customer_info.Tel_No,
    'emergency_number': customer_info.Emergency_Number,
    'birthday': customer_info.Birthday,
    'gender': customer_info.Gender,
  }

  context = {
    'customer_info': customer_info,
    'form': form,
  }
  return render(request, 'user/customer_info_update.html', context)



def customer_profile(request):

  customer_info = Customer_Info.objects.get(user=request.user)
  context = {
    'customer_info': customer_info,
  }
  return render(request, 'user/customer_profile.html', context)