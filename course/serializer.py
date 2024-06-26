from rest_framework import serializers
from . models import Course , Review


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name' , 'price' , 'description' , 'level' , 'period' , 'created_at' , 'updated_at' , 'is_active']



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['course' , 'rating' , 'comment']