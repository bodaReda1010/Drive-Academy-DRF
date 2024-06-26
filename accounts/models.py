from django.db import models
from django.contrib.auth.models import User
import uuid
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


def upload_account_image(instance , file_name):
    extension = file_name.split('.')[1]
    return f'Accounts/{instance.user}.{extension}'

class Account(models.Model):
    id = models.UUIDField(primary_key = True , default = uuid.uuid4 , editable = False)
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254 , unique = True)
    image = models.ImageField(upload_to=upload_account_image, height_field=None, width_field=None, max_length=None , null = True , blank = True)
    phone_number = models.CharField(max_length=50)


    class Meta:
        verbose_name = ("Account")
        verbose_name_plural = ("Accounts")

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Account.objects.create(user=instance)

    def __str__(self):
        return str(self.user)


@receiver(post_save , sender =settings.AUTH_USER_MODEL)
def token_create(sender , instance , created , **kwargs):
    if created:
        Token.objects.create(user = instance)


