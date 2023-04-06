from django.contrib import admin
from .models import Degree



class DegreeAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")
    search_fields = ("last_name",)


admin.site.register(Degree, DegreeAdmin)
