# coding:utf-8

from django.contrib import admin
from .models import Person, Child, DoctorChild
# from .forms import PersonForm


class ChildInline(admin.TabularInline):
    model = Child
    fields = ['name', 'age', 'date_birth', ]


# class DoctorInline(admin.TabularInline):
#     model = DoctorChild
#     # fields = ['name', 'category']


class ChildAdmin(admin.ModelAdmin):
    # inlines = [DoctorInline]
    list_display = ('name', 'person')
    list_filter = ('name', 'person')
    search_fields = ('name', 'person')
    filter_horizontal = ('doctors',)


class PersonAdmin(admin.ModelAdmin):
    inlines = [ChildInline]
    list_display = ('name', 'dni')
    list_filter = ('name', 'dni')
    search_fields = ('name', 'dni')


admin.site.register(Person, PersonAdmin)
admin.site.register(Child, ChildAdmin)
