from django.contrib import admin
from .models import (YearModel, MonthModel, WeekModel, Share)
# Register your models here.
admin.site.register(YearModel)
admin.site.register(MonthModel)
admin.site.register(Share)


@admin.register(WeekModel)
class WeekModelAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'month', 'year',
        'created_at',
    ]
