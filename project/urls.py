from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('api-accounts/' , include('accounts.urls' , namespace = 'accounts')),
    path('admin/', admin.site.urls),
    path('api-course/' , include('course.urls' , namespace = 'course')),
    path('api-trainers/' , include('trainers.urls' , namespace = 'trainers')),
    path('api-testimonials/' , include('testimonials.urls' , namespace = 'testimonials')),
    path('api-appointment/' , include('appointment.urls' , namespace = 'appointment')),
    path('api-token-auth/' , obtain_auth_token),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

