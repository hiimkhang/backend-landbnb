from django.contrib import admin
from . import models 
from django.contrib.auth.admin import UserAdmin

@admin.register(models.User) 
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile", # Title
            {
                "fields": (
                    "avatar",
                    "gender",
                    "birthday",
                    "language",
                    "superhost",
                    "bio",
                )
            },
        ),
    )
    pass

# admin.site.register(models.User, CustomUserAdmin)