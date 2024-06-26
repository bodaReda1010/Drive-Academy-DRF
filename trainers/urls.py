from django.urls import path
from . import views

app_name = 'trainers'

urlpatterns = [

    path('trainers_get_or_post/' , views.trainers_get_or_post , name = 'trainers_get_or_post'),
    path('trainers_get_or_put_or_delete/<str:id>/' , views.trainers_get_or_put_or_delete , name = 'trainers_get_or_put_or_delete'),

]