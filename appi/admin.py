from django.contrib import admin
from .models import players
class playeradmin(admin.ModelAdmin):
    list_display=('id','firstname','lastname','age','phone','signed')
admin.site.register(players,playeradmin)


# Register your models here.
