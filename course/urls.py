from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('course' , views.CourseViewset)
router.register('review' , views.ReviewViewset)

app_name = 'course'

urlpatterns = [

    path('course/<str:id>/rate_course/' , views.CourseViewset.as_view({'post':'rate_course'}) , name = 'rate_course')

]

urlpatterns += router.urls