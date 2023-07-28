from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from .models import User, ItemCategory, ListItem, ReviewReply,Request


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
    list_editable = ['name']
    list_per_page = 10


@admin.register(ListItem)
class ListItemAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "price", "category", "user"]
    list_editable = ["title","price"]
    list_per_page = 10
    list_select_related = ["category", "user"]
    
    

@admin.register(ReviewReply)
class ReviewReplyAdmin(admin.ModelAdmin):
    list_display = ['id','review','reply','date_created']
    
    
@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['id','task','owner','requester','status']