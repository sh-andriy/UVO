from django.contrib import admin
from .models import Project, Balance, Category


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "id")
    search_fields = ("name", "id")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "amount")
    search_fields = ("id", "user", "amount")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", 'category', 'reward')
    search_fields = ("id", "name", "description", 'category', 'reward')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
