# Jos rekisteröi tällä tavalla adminille oman appin
# modelit, voi myös admin sivuilta muokata näitä tietoja.

from django.contrib import admin

from app.models import Location, Car, Customer


@admin.register(Car)
class LocationAdmin(admin.ModelAdmin):
    pass

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass
