# coding:utf-8

from django.contrib import admin
from .models import Person, Child
# from .forms import PersonForm


class ChildInline(admin.TabularInline):
    model = Child
    fields = ['name', 'age', 'date_birth', ]


class ChildAdmin(admin.ModelAdmin):
    list_display = ('name', 'person')
    list_filter = ('name', 'person')
    search_fields = ('name', 'person')


class PersonAdmin(admin.ModelAdmin):
    inlines = [ChildInline]
    list_display = ('name', 'dni')
    list_filter = ('name', 'dni')
    search_fields = ('name', 'dni')


admin.site.register(Person, PersonAdmin)
admin.site.register(Child, ChildAdmin)
