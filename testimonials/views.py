from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes , authentication_classes
from rest_framework.permissions import IsAdminUser , IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from . models import Comment
from . serializer import CommentSerializer
from accounts.models import Account



@api_view(['GET'])
@permission_classes([IsAdminUser])
@authentication_classes([TokenAuthentication])
def get_all_comments(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments , many = True)
        json = {
            'Message':'All Comments: ',
            'Data':serializer.data
        }
        return Response(json , status = status.HTTP_200_OK)
    elif request.method == 'POST':
        profile = Account.objects.get(user=request.user)
        comment = request.data['comment']
        profession = request.data['profession']
        comment = Comment.objects.create(
            profile=profile,
            comment=comment,
            profession=profession,
        )

        serializer = CommentSerializer(comment)

        json = {
            'Message':'Comment Has Been Added: ',
            'Data':serializer.data
        }
        return Response(json , status = status.HTTP_201_CREATED)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def create_comment(request):
    profile = Account.objects.get(user=request.user)
    comment = request.data['comment']
    profession = request.data['profession']
    comment = Comment.objects.create(
        profile=profile,
        comment=comment,
        profession=profession,
    )

    serializer = CommentSerializer(comment)

    json = {
        'Message':'Comment Has Been Added: ',
        'Data':serializer.data
    }
    return Response(json , status = status.HTTP_201_CREATED)




@api_view(['GET' , 'PUT' , 'DELETE'])
@permission_classes([IsAdminUser])
@authentication_classes([TokenAuthentication])
def comment_get_or_put_or_delete(request , id):
    comment = Comment.objects.get(id=id)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        json = {
            'Message':'The Comment Is: ',
            'Data':serializer.data
        }
        return Response(json , status = status.HTTP_200_OK)
    elif request.method == 'PUT':
        comment_user = request.data['comment']
        profession = request.data['profession']

        comment.comment = comment_user
        comment.profession = profession
        comment.save()
        serializer = CommentSerializer(comment)

        json = {
            'Message':'The Comment Has Been Updated: ',
            'Data':serializer.data
        }
        return Response(json , status = status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        comment.delete()
        return Response({'Message':'Comment Has Been Deleted'} , status = status.HTTP_200_OK)