from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name= 'tour'),
    path('<int:tour_id>',views.detail, name= 'detail'), 
    path('search',views.search, name= 'search'),
    path('reservation/<int:tour_id>',views.reservation, name= 'reservation'),
    path('make_reservation/<int:tour_id>',views.make_reservation, name='make_reservation'),
]