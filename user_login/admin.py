from django.contrib import admin

# Register your models here.
from .models import Sign_up

class Sign_upAdmin(admin.ModelAdmin):
    list_display = ("username","email","password")

admin.site.register(Sign_up,Sign_upAdmin)
