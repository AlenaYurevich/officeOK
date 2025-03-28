from django.contrib import admin
from .models import Category, Product, ProductImage, Brand, Section


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 4  # Количество пустых форм для добавления изображений


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Поля для отображения в списке
    search_fields = ('name',)  # Поля для поиска
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')  # Поля для отображения в списке
    search_fields = ('name',)  # Поля для поиска
    ordering = ('-created_at',)  # Сортировка


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ('name', 'category', 'sections_list', 'brand', 'price', 'available', 'created', 'updated')
    list_filter = ['category', 'available', 'created', 'updated']
    filter_horizontal = ('sections',)  # Добавит удобный интерфейс выбора
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'article')

    def sections_list(self, obj):
        return ", ".join([s.name for s in obj.sections.all()])

    sections_list.short_description = "Разделы"
