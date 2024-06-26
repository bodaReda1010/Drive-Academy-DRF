from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes , authentication_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import TokenAuthentication
from . models import Trainer
from . serializer import TrainerSerializer


@api_view(['GET' , 'POST'])
@permission_classes([IsAdminUser])
@authentication_classes([TokenAuthentication])
def trainers_get_or_post(request):
    if request.method == 'GET':
        trainers = Trainer.objects.all()
        serializer = TrainerSerializer(trainers , many = True)
        json = {
            'Message':'Data For All Trainers: ',
            'Data':serializer.data
        }
        return Response(json , status = status.HTTP_200_OK)
    elif request.method == 'POST':
        name = request.data['name']
        trainer = Trainer.objects.create(name=name)
        serializer = TrainerSerializer(trainer)
        json = {
            'Message':'One Trainer Has Been Added: ',
            'Data':serializer.data
        }
        return Response(json , status = status.HTTP_201_CREATED)


@api_view(['GET' , 'DELETE'])
@permission_classes([IsAdminUser])
@authentication_classes([TokenAuthentication])
def trainers_get_or_put_or_delete(request , id):
    trainer = Trainer.objects.get(id=id)
    if request.method == 'GET':
        serializer = TrainerSerializer(trainer)
        json = {
            'Message':'Data Belongs To Trainer With This Id: ',
            'Data':serializer.data
        }
        return Response(json , status = status.HTTP_200_OK)
    elif request.method == 'DELETE':
        trainer.delete()
        json = {
            'Message':'Trainer With This ID Has Been Deleted: ',
        }
        return Response(json , status = status.HTTP_200_OK)