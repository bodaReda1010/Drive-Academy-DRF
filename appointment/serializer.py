from rest_framework import serializers
from . models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['name' , 'email' ,'course_name' , 'car_type' , 'message']