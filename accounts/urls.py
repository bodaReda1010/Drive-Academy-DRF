from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [

    path('signup/' , views.signup , name = 'signup'),
    path('get_user_info/' , views.get_user_info , name = 'get_user_info'),
    path('reset_password/' , views.reset_password , name = 'reset_password'),
    path('edit_profile/' , views.edit_profile , name = 'edit_profile'),

]