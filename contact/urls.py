from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [

    path('contact/',views.contact,name='contact'),
    path('get_all_contacts/',views.get_all_contacts,name='get_all_contacts'),
    
]