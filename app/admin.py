from django.contrib import admin
from .models import *

class LocationAdmin(admin.ModelAdmin):
    list_display= ("line1", "line2", "postCode", "googleLocation")

class DeviceAdmin(admin.ModelAdmin):
    list_display= ("unitID1", "unitID2", "location", "locationDescription")

admin.site.register(Location, LocationAdmin)
admin.site.register(Device, DeviceAdmin)