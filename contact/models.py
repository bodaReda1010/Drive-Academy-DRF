from django.db import models
from accounts.models import Account
import uuid
# Create your models here.


class Contact(models.Model):
    id = models.UUIDField(primary_key = True , default = uuid.uuid4 , editable = False)
    account = models.ForeignKey(Account , on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50)
    message = models.TextField()

    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")

    def __str__(self):
        return str(self.account)