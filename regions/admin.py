from django.contrib import admin
from regions.models import Region, Commune


class RegionAdmin(admin.ModelAdmin):
    list_display = ('region_name',)
    search_fields = ('region_name',)

class CommuneAdmin(admin.ModelAdmin):
    list_display = ('commune_name',)
    search_fields = ('commune_name',)


admin.site.register(Region, RegionAdmin)
admin.site.register(Commune, CommuneAdmin)