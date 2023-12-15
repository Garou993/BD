from django.contrib import admin

from .models import (Client, 
Services, 
PcBuilder, 
PcMaster, 
PcCleaner, 
Orders, 
ItemsForOrder,
Invoices, 
Indtracks, 
Industries, 
InvoiceItems,
ClientCommentCourier,
ClientCommentDevices,
ClientCommentMaster,
BuilderStatus,
CleanerStatus,
MasterStatus,
Flash,
Hdd,
Ssd,
Microphones,
Mice,
Keyboards,
Items,
Couriers,
PickUpPoint,
Storage,
Cars
)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.contrib.admin import AdminSite
from django.utils.translation import gettext

admin.site.site_header = "Меню Администрирования"
admin.site.site_url = "../login"


admin.site.register(Client)
admin.site.register(Services)
admin.site.register(PcBuilder)
admin.site.register(PcMaster)
admin.site.register(PcCleaner)
admin.site.register(Orders)
admin.site.register(Invoices)
admin.site.register(Indtracks)
admin.site.register(Industries)
admin.site.register(InvoiceItems)

admin.site.register(ItemsForOrder)
admin.site.register(ClientCommentCourier)
admin.site.register(ClientCommentDevices)
admin.site.register(ClientCommentMaster)
admin.site.register(BuilderStatus)
admin.site.register(CleanerStatus)
admin.site.register(MasterStatus)
admin.site.register(Flash)
admin.site.register(Hdd)
admin.site.register(Ssd)
admin.site.register(Microphones)
admin.site.register(Mice)
admin.site.register(Keyboards)
admin.site.register(Items)
admin.site.register(PickUpPoint)
admin.site.register(Couriers)
admin.site.register(Storage)
admin.site.register(Cars)
# admin.site.register(Industries)
