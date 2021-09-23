from django.contrib import admin
from .models import Details
from django.db.models.functions import Lower

# Register your models here.


class DetailsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

    def get_ordering(self, request):
        return [Lower('name')]  # sort case insensitive


admin.site.register(Details, DetailsAdmin)