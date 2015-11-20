from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from .models import Colors, Categories, Tags, Notes


class CategoriesAdmin(MPTTModelAdmin):
    tree_title_field = 'name'
    tree_display = ('name',)


admin.site.register(Notes)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Colors)
admin.site.register(Tags)