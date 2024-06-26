from django.urls import path
from . import views

app_name = 'testimonials'

urlpatterns = [

    path('get_all_comments/' , views.get_all_comments , name = 'get_all_comments'),
    path('create_comment/' , views.create_comment , name = 'create_comment'),
    path('comment_get_or_put_or_delete/<str:id>/' , views.comment_get_or_put_or_delete , name = 'comment_get_or_put_or_delete'),

]