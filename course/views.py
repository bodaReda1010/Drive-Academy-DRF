from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets , status
from rest_framework.response import Response
from . models import Course , Review
from . serializer import CourseSerializer , ReviewSerializer
from django.contrib.auth.models import User


class CourseViewset(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]


    # http://127.0.0.1:8000/api-course/course/course_id/rate_course/
    @action(detail=True , methods=['POST'])
    def rate_course(self , request , id = None):
        if 'rating' in request.data:
            course = Course.objects.get(id = id)
            username = request.data['username']
            user = User.objects.get(username = username)
            stars = request.data['rating']
            comment = request.data['comment']
            try:
                rating = Review.objects.get(course = course)
                rating.rating = stars
                rating.comment = comment
                rating.save()
                serializer = ReviewSerializer(rating)
                response = {
                    'Message':'Review Updated',
                    'result':serializer.data
                }
                return Response(response , status = status.HTTP_200_OK)
            except:
                rating = Review.objects.create(course = course , comment = comment , user = user , rating = stars)
                serializer = ReviewSerializer(rating)
                response = {
                    'Message':'Review Created',
                    'result':serializer.data
                }
                return Response(response , status = status.HTTP_201_CREATED)




class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def create(self, request, *args, **kwargs):
        response = {
            'Message': 'Create From Here Is Denied'
        }
        return Response(response , status = status.HTTP_204_NO_CONTENT)
    
    def update(self, request, *args, **kwargs):
        response = {
            'Message': 'Update From Here Is Denied'
        }
        return Response(response , status = status.HTTP_204_NO_CONTENT)
    
    def retrieve(self, request, *args, **kwargs):
        response = {
            'Message': 'Retrieve From Here Is Denied'
        }
        return Response(response , status = status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, *args, **kwargs):
        response = {
            'Message': 'Destroy From Here Is Denied'
        }
        return Response(response , status = status.HTTP_204_NO_CONTENT)

