from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.
@admin.register(models.HouseType)
class ItemAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Amenity)
class AmenityAdmin(admin.ModelAdmin):
    # class Bathroom(models.):
    #     name = "Bathroom"
    
    # class Bedroom_Laundry(admin.ModelAdmin):
    #     name = "Bedroom and laundry"
    #     def __str__(self):
    #         return self.name
    #     pass

    # class Heating_Cooling(admin.ModelAdmin):
    #     name = "Heating and cooling"
    #     def __str__(self):
    #         return self.name
    #     pass
    
    # fieldsets = (
    #     (
    #         "Bathroom", {"fields": ()}
    #     ),
    #     (
    #         "Bedroom and laundry", {"fields": ()}
    #     ),
    #     (
    #         "Heating and cooling", {"fields": ()}
    #     ),
    #     (
    #         "Home safety", {"fields": ()}
    #     ),
    # )
    pass

@admin.register(models.Facility)
class FacilityAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("__str__", "get_thumbnail",)
    
    def get_thumbnail(self, obj):
        return mark_safe(f"<img width=50px src= \"{obj.file.url}\">/")
    get_thumbnail.short_description = "Thumbnail"

class PhotoInline(admin.TabularInline):
    model = models.Photo
@admin.register(models.House)
class HouseAdmin(admin.ModelAdmin):
    inlines = (PhotoInline,)

    list_display = (
        "name",
        "truncated_description",
        "country",
        "city",
        "price",
        "guest",
        "bedroom",
        "bed",
        "bathroom",
        "check_in",
        "check_out",
        "amenities_count",
        "total_rating",
    )

    list_filter = (
        "house_type",
        "amenities",
        "facilities",
        "city",
        "country",
    )

    search_fields = [
        "city",
        "^host__username",
        "=price",
        "^name",
    ]

    filter_horizontal = (
        "amenities",
        "facilities",
    )

    # ordering = (
    #     "name",
    #     "price"
    # )

    raw_id_fields = ("host",)

    # def AmenityCount(self, obj):
    #     return obj.amenities.count()
    # AmenityCount.short_description = "amenities"