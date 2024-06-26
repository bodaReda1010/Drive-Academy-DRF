from django.contrib import admin
from . models import Course , Review
# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name' , 'price' , 'level' , 'period' , 'created_at' , 'updated_at' , 'is_active']
    


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user' , 'course' , 'rating' , 'comment']