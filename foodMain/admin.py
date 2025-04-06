from django.contrib import admin
from .models import Food, Categories

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("title", "isUpdate", "short_description", "date", "slug", "category_list")
    list_display_links = ("title", "slug")
    prepopulated_fields = {"slug": ("title",),}
    list_filter = ("title", "isUpdate")
    list_editable = ("isUpdate",)
    search_fields = ("title", "slug")

    def category_list(self, obj):
        html = ""
        for category in obj.categories.all():
            html += category.name + " "
        return html

    def short_description(self, obj):
            if len(obj.description) > 50:
                return obj.description[:50] + '...'
            else:
                return obj.description

    short_description.short_description = 'Description'

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "recipe_count")
    list_display_links = ("name","slug")
    list_filter = ("slug",)
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}

    def recipe_count(self, obj):
        return obj.food_set.count()