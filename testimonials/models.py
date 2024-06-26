from django.db import models
import uuid
from accounts.models import Account
# Create your models here.


class Comment(models.Model):
    id = models.UUIDField(primary_key = True , default = uuid.uuid4 , editable = False)
    profile = models.ForeignKey(Account , on_delete=models.CASCADE)
    comment = models.TextField()
    profession = models.CharField(max_length=50)


    class Meta:
        verbose_name = ("Comment")
        verbose_name_plural = ("Comments")

    def __str__(self):
        return str(self.profile)