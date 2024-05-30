from django.urls import path
from . import views




urlpatterns = [
    path('login/',views.login,name='login'),
    path('register/',views.register, name='register'),
    path('logout/',views.logout, name='logout'),
    path('payment/',views.payment, name= 'payment'),
    path('make_payment/', views.make_payment, name='make_payment'),
    path('travel_history/',views.travel_history, name= 'travel_history'),
    path('customer_info_update/',views.customer_info_update, name= 'customer_info_update'),
    path('customer_profile/',views.customer_profile, name= 'customer_profile'),
]