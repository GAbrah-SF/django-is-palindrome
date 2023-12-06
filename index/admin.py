from django.contrib import admin
from .models import Palindroma


# Register your models here.
@admin.register(Palindroma)
class TablaPalabrasPalindromas(admin.ModelAdmin):
    list_display = ('id', 'palabra')
