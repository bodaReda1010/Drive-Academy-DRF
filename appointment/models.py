from django.db import models
import uuid
from accounts.models import Account
from course.models import Course



class Appointment(models.Model):
    id = models.UUIDField(primary_key = True , default = uuid.uuid4 , editable = False)
    name = models.ForeignKey(Account , on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    course_name = models.ForeignKey(Course , on_delete=models.CASCADE)
    car_type = models.CharField(max_length=50)
    message = models.TextField()

    

    class Meta:
        verbose_name = ("Appointment")
        verbose_name_plural = ("Appointments")

    def __str__(self):
        return str(self.name)