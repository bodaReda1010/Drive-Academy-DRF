from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view , permission_classes , authentication_classes
from . models import Appointment , Account , Course
from . serializer import AppointmentSerializer



@api_view(['GET'])
@permission_classes([IsAdminUser])
@authentication_classes([TokenAuthentication])
def get_all_appointments(request):
    appointments = Appointment.objects.all()
    my_serializer = AppointmentSerializer(appointments , many = True)
    json = {
        'Message':'All Appointments: ',
        'Data':my_serializer.data,
    }
    return Response(json , status = status.HTTP_200_OK)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def appointment(request):
    name = Account.objects.get(user = request.user)
    email = name.email
    course_name = Course.objects.get(name = request.data['course_name'])
    car_type = request.data['car_type']
    message = request.data['message']
    try:
        my_appointment = Appointment.objects.create(
            name = name,
            email = email,
            course_name = course_name,
            car_type = car_type,
            message = message,
        )
        my_serializer = AppointmentSerializer(my_appointment)
        json = {
        'Message':'Success , Your Appointment Has Been Booked: ',
        'Data':my_serializer.data,
        }
        return Response(json , status = status.HTTP_201_CREATED)
    except:
        return Response({"ERROR":"Can't Post Your Account , Try Again"} , status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET' , 'PUT' , 'DELETE'])
@permission_classes([IsAdminUser])
@authentication_classes([TokenAuthentication])
def appointment_get_or_put_or_delete(request , id):
    my_appointment = Appointment.objects.get(id=id)
    if request.method == 'GET':
        serializer = AppointmentSerializer(my_appointment)
        json = {
            'Message':'The Appointment With This ID: ',
            'Data':serializer.data,
        }
        return Response(json , status = status.HTTP_200_OK)
    elif request.method == 'PUT':
        course_name = Course.objects.get(name = request.data['course_name'])
        car_type = request.data['car_type']
        message = request.data['message']

        my_appointment.course_name = course_name
        my_appointment.car_type = car_type
        my_appointment.message = message
        my_appointment.save()

        serializer = AppointmentSerializer(my_appointment)

        json = {
            'Message':'The Appointment With This ID Has Been Updated:',
            'Data':serializer.data,
        }

        return Response(json , status = status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        my_appointment.delete()
        return Response({'Message':'The Appointment With This ID Has Been Deleted:'} , status = status.HTTP_200_OK)


