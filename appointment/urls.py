from django.urls import path
from . import views

app_name = 'appointment'

urlpatterns = [

    path('get_all_appointments/' , views.get_all_appointments , name = 'get_all_appointments'),
    path('appointment/' , views.appointment , name = 'appointment'),
    path('appointment_get_or_put_or_delete/<str:id>/' , views.appointment_get_or_put_or_delete , name = 'appointment_get_or_put_or_delete'),

]

