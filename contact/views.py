from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes , authentication_classes
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from rest_framework.authentication import TokenAuthentication
from . models import Contact
from . serializer import ContactSerializer
from accounts.models import Account
from django.core.mail import send_mail
from django.conf import settings



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def contact(request):
    if request.method == 'POST':
        account = Account.objects.get(user = request.user)
        email = request.data['email']
        subject = request.data['subject']
        message = request.data['message']

        contact = Contact.objects.create(
            account = account,
            email = email,
            subject = subject,
            message = message,
        )
        send_mail(
                message,
                subject,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently = False,
        )
        serializer = ContactSerializer(contact)

        json = {
            'Message':'Your Message Has Been Sent',
            'Data':serializer.data
        }
        return Response(json , status = status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAdminUser])
@authentication_classes([TokenAuthentication])
def get_all_contacts(request):
    contacts = Contact.objects.all()
    serializer = ContactSerializer(contacts , many = True)
    json = {
        'Message':'All Contacts',
        'Data':serializer.data
    }
    return Response(json , status = status.HTTP_200_OK)