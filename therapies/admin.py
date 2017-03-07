# coding:utf-8
from django.contrib import admin
from .models import Therapie, Time


class TimeInline(admin.TabularInline):
    model = Time


class TherapieAdmin(admin.ModelAdmin):
    inlines = [TimeInline]
    list_display = ('doctors', 'terapy')
    list_filter = ('doctors', 'terapy')
    search_fields = ('doctors', 'terapy')


admin.site.register(Therapie, TherapieAdmin)
