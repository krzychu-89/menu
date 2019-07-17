from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe
from .serializers import convert_datetime
from .models import *


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    readonly_fields = ["data_dodania", "data_modyfikacji"]

    def data_dodania(self, obj):
        return convert_datetime(obj.created)

    def data_modyfikacji(self, obj):
        return convert_datetime(obj.modified)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    readonly_fields = ["dish_image", "data_dodania",
                       "data_modyfikacji"]

    def dish_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.image.url,
            width=obj.image.width,
            height=obj.image.height,
            )
    )

    def data_dodania(self, obj):
        return convert_datetime(obj.created)

    def data_modyfikacji(self, obj):
        return convert_datetime(obj.modified)