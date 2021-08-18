from django.db import models
from django.db.models.fields import NullBooleanField

# Create your models here.


class BillingItem(models.Model):
    item_name = models.CharField(max_length=40, null=True, blank=True)
    number_1 = models.IntegerField()
    number_2 = models.IntegerField()
    total = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.total)
