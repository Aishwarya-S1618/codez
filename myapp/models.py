from django.db import models
from django.db.models.functions import Lower


# Create your models here.


class Details(models.Model):
    name = models.CharField(max_length=20, default='', null=False)
    email = models.CharField(max_length=30, default='', null=False)
    phone = models.CharField(max_length=10, default='', null=False)
    comment = models.CharField(max_length=200, default='', null=False)
    def __str__(self):
        return self.name


#Details.objects.all().order_by('-phone')


'''
class MyModelAdmin(Details):
    list_display = ('name',)
    search_fields = ['name']

    def get_ordering(self, request):
        return [Lower('name')]  # sort case insensitive

'''