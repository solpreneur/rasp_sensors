from django.contrib import admin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .models import ReadingTypes,Reading


# Register your models here.
@admin.register(ReadingTypes)
class ReadingTypes(admin.ModelAdmin):
    list_display = ("id", "reading_type")

@admin.register(Reading)
class Reading(admin.ModelAdmin):
    list_display = ("read_type","value","date_time")
    list_filter = ('read_type',('date_time', DateRangeFilter), ('date_time', DateTimeRangeFilter))
    search_fields = ('read_type',)
    ordering = ('-date_time',)
    list_per_page = 100