from django.db import models
import uuid
# Create your models here.


def upload_trainer_image(instance , file_name):
    extension = file_name.split('.')[1]
    return f'Trainer/{instance.name}.{extension}'


class Trainer(models.Model):
    id = models.UUIDField(primary_key = True , default = uuid.uuid4 , editable = False)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to=upload_trainer_image, height_field=None, width_field=None, max_length=None , null = True , blank = True)

    class Meta:
        verbose_name = ("Trainer")
        verbose_name_plural = ("Trainers")

    def __str__(self):
        return self.name
