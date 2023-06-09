from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from .models import User, ItemCategory, ListItem


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("id", "email", "username", "password1", "phone"),
            },
        ),
    )


@admin.register(ItemCategory)
class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "icon", "backgroundColor", "color"]
    list_per_page = 10


@admin.register(ListItem)
class ListItemAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "price", "category", "user"]
    list_editable = ["title","price"]
    list_per_page = 10
    list_select_related = ["category", "user"]