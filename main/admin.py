# from tkinter import Widget
from django.contrib import admin
from django.contrib.admin.widgets import AdminTextareaWidget, AdminTextInputWidget
from django.urls import clear_script_prefix
from parler.admin import TranslatableAdmin, TranslatableStackedInline, TranslatableTabularInline
from parler.forms import TranslatableModelForm, TranslatedField
from .models import *


# Stacked ADMINS
class ProductImageStacked(TranslatableStackedInline):
    model = ProductImages
    extra = 1

class ProductStacked(TranslatableStackedInline):
    model = Product
    extra = 1

class AddBlockItemStacked(TranslatableStackedInline):
    model = AddBlockItem
    extra = 1

class CategoryImageStacked(TranslatableStackedInline):
    model = CategoryImage
    extra = 1

class AdditionalFormValueStacked(TranslatableStackedInline):
    model = AdditionalFormValue
    extra = 1

class ProductAdminForm(TranslatableModelForm):
    name = TranslatedField(widget=AdminTextInputWidget)
    content = TranslatedField(widget=AdminTextareaWidget)





class ProductAdmin(TranslatableAdmin):
    inlines = [ProductImageStacked]
    list_display = ("name", "id")
    form = ProductAdminForm
    fieldsets = ((None,{"fields": ("name", "sizing", "slug", "price", "description", "category", "image"),},),)

    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ("name",)}


class AdditionalFormValueAdmin(TranslatableAdmin):
    list_display = ("name", "id")
    list_display_links = ("name", "id")
    fieldsets = ((None,{"fields": ("product", 'type',"name", "placeholder"),},),)

# class CategoryAdminForm(TranslatableModelForm):
    # name = TranslatedField(widget=AdminTextInputWidget)
    # slug = TranslatedField(widget=AdminTextInputWidget)
    # image = TranslatedField(widget=Admin)
    # description = TranslatedField(widget=AdminTextareaWidget)
    # additional = TranslatedField(widget=AdminTextInputWidget)   
    

class CategoryAdmin(TranslatableAdmin):
    inlines = [AddBlockItemStacked, CategoryImageStacked]
    list_display = ("name","id")
    # form = CategoryAdminForm
    fieldsets = ((None,{"fields": ("name", "slug", "image","description", "additional"),},),)

    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ("name",)}

class CategoryImagesAdmin(TranslatableAdmin):
    list_display = ("image","category" ,"id")
    list_display_links = ("image","category" ,"id")


class ProductImagesAdmin(TranslatableAdmin):
    list_display = ("image","product" ,"id")
    list_display_links = ("image","product" ,"id")


class AddBlockItemAdmin(TranslatableAdmin):
    list_display = ("name","category" ,"id")
    list_display_links = ("name","category" ,"id")


# class CategoryAdminForm(TranslatableModelForm):
    # name = TranslatedField(widget=AdminTextInputWidget)
    # name = TranslatedField(widget=AdminTextInputWidget)


# class CategoryAdmin(TranslatableAdmin):
#     inlines = [ProductStacked]
#     list_display = ("name",'id')
#     # form = CategoryAdminForm

#     fieldsets = (
#         (
#             None,
#             {
#                 "fields": ("name",),
#             },
#         ),
#     )

class AboutItemAdmin(TranslatableAdmin):
    list_display = ["title", "body", "image", "id"]
    list_display = ("body","image")
    fieldsets = ((None,{"fields": ("title","body", "image"),},),)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["name", "product", "id"]
    list_display_links = ["name", "product", "id"]


@admin.register(ClientMessage)
class ClientMessageAdmin(admin.ModelAdmin):
    list_display = ["name","phone", 'id']
    list_display_links = ["name", "phone", "id"]    


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImages, ProductImagesAdmin)
admin.site.register(CategoryImage, CategoryImagesAdmin)
admin.site.register(AddBlockItem, AddBlockItemAdmin)
admin.site.register(AboutItem, AboutItemAdmin)
admin.site.register(AdditionalFormValue, AdditionalFormValueAdmin)
admin.site.register(Creator)











# admin.site.register(StackedCategory, CategoryStackedAdmin)
# admin.site.register(TabularCategory, CategoryTabularAdmin)
