# coding:utf-8

from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    filter_horizontal = ('doctors',)


admin.site.register(Category, CategoryAdmin)
