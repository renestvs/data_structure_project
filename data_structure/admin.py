from django.contrib import admin
from data_structure.models import Serie
from data_structure.models import Datum

class serieAdmin(admin.ModelAdmin):
    model = Serie

class datumAdmin(admin.ModelAdmin):
    model = Datum

admin.site.register(Serie, serieAdmin)
admin.site.register(Datum, datumAdmin)
