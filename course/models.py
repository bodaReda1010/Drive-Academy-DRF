from django.db import models
from django.utils.text import slugify
import uuid
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator , MaxValueValidator
from django.core.exceptions import ValidationError
# Create your models here.



def upload_course_image(instance , file_name):
    extension = file_name.split('.')[1]
    return f'Course/{instance.name}.{extension}'


LEVEL = (
    ('Beginner','Beginner'),
    ('Mid-Level','Mid-Level'),
    ('Expert','Expert'),
)


class Course(models.Model):
    id = models.UUIDField(primary_key = True , default = uuid.uuid4 , editable = False)
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to=upload_course_image, height_field=None, width_field=None, max_length=None , null = True, blank = True)
    price = models.FloatField(default = 0)
    description = models.TextField()
    level = models.CharField(max_length=100,choices=LEVEL)
    period = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default = True)

    class Meta:
        verbose_name = ("Course")
        verbose_name_plural = ("Courses")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Course , self).save(*args, **kwargs)

    def num_of_rating(self):
        rating = Review.objects.filter(course = self)
        return len(rating)
    
    def avg(self):
        rating = Review.objects.filter(course = self)
        stars = 0
        for x in rating:
            start += x.rating
        if len(rating) > 0:
            return stars / len(rating)
        return 0


    def __str__(self):
        return self.name



class Review(models.Model):
    id = models.UUIDField(primary_key = True , default = uuid.uuid4 , editable = False)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    course = models.ForeignKey(Course , on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment = models.TextField()

    def clean(self):
        if self.rating < 1:
            raise ValidationError('Rating Min Value Must Be Greater Than 1')
        if self.rating > 5:
            raise ValidationError('Rating Max Value Must Be Smaller Than 5')
        return super(Review , self).clean()

    class Meta:
        unique_together = (('user' , 'course'),)
        index_together = (('user' , 'course'),)

    class Meta:
        verbose_name = ("Review")
        verbose_name_plural = ("Reviews")

    def __str__(self):
        return f'Review Of {self.course}'