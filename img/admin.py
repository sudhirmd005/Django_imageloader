from django.contrib import admin
from .models import Imageloader

@admin.register(Imageloader)
# admin.site.register(Imageloader)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo','date']