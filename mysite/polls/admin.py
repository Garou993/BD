from django.contrib import admin

from .models import Client, Services, PcBuilder, PcMaster, PcCleaner

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.contrib.admin import AdminSite
from django.utils.translation import gettext

admin.site.site_header = "Administration menu"


admin.site.register(Client)
admin.site.register(Services)
admin.site.register(PcBuilder)
admin.site.register(PcMaster)
admin.site.register(PcCleaner)