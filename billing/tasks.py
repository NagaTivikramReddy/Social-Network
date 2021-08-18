from __future__ import absolute_import, unicode_literals
import random
from celery.decorators import task
from .models import BillingItem


@task(name="sum_two_numbers")
def add(x, y):
    return x + y


@task(name="multiply_two_numbers")
def mul(x, y):
    total = x * (y * random.randint(3, 100))
    new_obj = BillingItem.objects.create(
        item_name='bill', number_1=x, number_2=y, total=total)
    new_obj.save()
    return total


@task(name="sum_list_numbers")
def xsum(numbers):
    return sum(numbers)
