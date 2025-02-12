from django.conf import settings
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin

from api.models import PatientProfile, HeartData

admin.site.register(settings.AUTH_USER_MODEL,UserAdmin)

admin.site.register(PatientProfile,ModelAdmin)
admin.site.register(HeartData,ModelAdmin)

