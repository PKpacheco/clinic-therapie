# coding:utf-8

from django.contrib import admin
from .models import Doctor


class DoctorAdmin(admin.ModelAdmin):
    list_filter = ('name', 'category')
    search_fields = ('name', 'category')
    filter_horizontal = ('category',)


admin.site.register(Doctor, DoctorAdmin)
