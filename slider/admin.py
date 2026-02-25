from django.contrib import admin
from django.utils.html import format_html

from adminsortable2.admin import SortableAdminMixin

from slider.models.sliders import Slider

from unfold.admin import ModelAdmin


@admin.register(Slider)
class SliderAdmin(ModelAdmin, SortableAdminMixin):
    ordering_field = "order"
    hide_ordering_field = True
    list_display = ["thumbnail", "title", "is_active"]

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="50"/>', obj.image.url)
        return "-"

    thumbnail.short_description = "Превью"
