from django.contrib import admin
from .models import MinervaUser
# Register your models here.

@admin.register(MinervaUser)
class MinervaUserAdmin(admin.ModelAdmin):
    pass