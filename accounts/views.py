from rest_framework import status
from rest_framework.decorators import api_view , permission_classes , authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from . serializer import UserSerializer , RegisterSerializer , EditProfileSerializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password



@api_view(['POST'])
def signup(request):
    username = request.data['email'].split('@')[0]
    first_name = request.data['first_name']
    last_name = request.data['last_name']
    email = request.data['email']
    password = request.data['password']

    if not User.objects.filter(username=username).exists():
        user = User.objects.create(
            username    = username,
            first_name  = first_name,
            last_name   = last_name,
            email       = email,
            password    = make_password(password)
        )
        serializer = RegisterSerializer(user)
        json = {
            'Message': 'Successfully Registered',
            'Data': serializer.data
        }
        return Response(json , status = status.HTTP_201_CREATED)
    return Response({'ERROR!!!':'This User Allready Has An Account'} , status = status.HTTP_400_BAD_REQUEST)





@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def get_user_info(request):
    user = request.user
    serializer = UserSerializer(user)
    json = {
        'User Data': serializer.data
    }
    return Response(json , status = status.HTTP_200_OK)




@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def reset_password(request):
    user = request.user
    password = request.data['password']
    confirm_password = request.data['confirm_password']

    if password == confirm_password:
        user.set_password(password)
        user.save()
        json = {
            'Done': 'Password Has Been Reseted Successfully',
            'Message':f'The New Password Is {password}'
        }
        return Response(json , status = status.HTTP_200_OK)
    return Response({'ERROR!!!':'The Password Must Be The Same Of Confirm Password'} , status = status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def edit_profile(request):
    user = request.user
    user.username = request.data['username']
    user.first_name = request.data['first_name']
    user.last_name = request.data['last_name']
    user.email = request.data['email']
    user.save()
    serializer = EditProfileSerializer(user)
    json = {
        'Message':'Edit Profile Has Been Done',
        'Data':serializer.data
    }
    return Response(json , status = status.HTTP_200_OK)