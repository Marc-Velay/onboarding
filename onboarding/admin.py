from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import UserContact


@admin.register(UserContact)
class TRCancelAdmin(admin.ModelAdmin):
                list_display = ('first_name', 'last_name', 'nationality', 'dob', 'doe', 'sex', 'dni')
