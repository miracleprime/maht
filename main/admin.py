from django.contrib import admin
from django.db import models
from django.utils.html import format_html
from django_ckeditor_5.widgets import CKEditor5Widget

from .models import (
    Service, Portfolio, ContactInfo, Order,
    DeliveryInfo, PaymentInfo, TermsInfo, ContentBlock, SiteSettings
)



class CKEditorAdminMixin:
    ckeditor_fields = ()

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if isinstance(db_field, models.TextField) and db_field.name in self.ckeditor_fields:
            kwargs['widget'] = CKEditor5Widget()
        return super().formfield_for_dbfield(db_field, request, **kwargs)


class ImagePreviewMixin:
    @admin.display(description='Превью')
    def image_preview(self, obj):
        if getattr(obj, 'image', None):
            return format_html(
                '<img src="{}" style="max-height:60px; max-width:90px; border-radius:8px;" />',
                obj.image.url
            )
        return 'Нет фото'


@admin.register(Service)
class ServiceAdmin(CKEditorAdminMixin, ImagePreviewMixin, admin.ModelAdmin):
    list_display = ('title', 'price', 'order', 'image_preview')
    list_editable = ('order',)
    search_fields = ('title', 'description', 'price')
    ordering = ('order', 'id')
    ckeditor_fields = ('description',)
    fieldsets = (
        ('Основное', {
            'fields': ('title', 'price', 'description')
        }),
        ('Изображение', {
            'fields': ('image',)
        }),
        ('Порядок', {
            'fields': ('order',)
        }),
    )


@admin.register(Portfolio)
class PortfolioAdmin(CKEditorAdminMixin, ImagePreviewMixin, admin.ModelAdmin):
    list_display = ('title', 'category', 'order', 'image_preview')
    list_editable = ('order',)
    search_fields = ('title', 'category', 'description')
    ordering = ('order', 'id')
    ckeditor_fields = ('description',)
    fieldsets = (
        ('Основное', {
            'fields': ('title', 'category', 'description')
        }),
        ('Изображение', {
            'fields': ('image',)
        }),
        ('Порядок', {
            'fields': ('order',)
        }),
    )


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Контакты', {
            'fields': ('phone', 'email', 'address')
        }),
        ('Дополнительно', {
            'fields': ('work_hours', 'map_link')
        }),
    )

    def has_add_permission(self, request):
        if ContactInfo.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'created_at', 'is_processed')
    list_editable = ('is_processed',)
    list_filter = ('is_processed', 'created_at')
    search_fields = ('name', 'phone', 'email', 'comment')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    fieldsets = (
        ('Клиент', {
            'fields': ('name', 'phone', 'email')
        }),
        ('Комментарий', {
            'fields': ('comment',)
        }),
        ('Статус', {
            'fields': ('is_processed', 'created_at')
        }),
    )


@admin.register(DeliveryInfo)
class DeliveryInfoAdmin(CKEditorAdminMixin, ImagePreviewMixin, admin.ModelAdmin):
    list_display = ('title', 'order', 'image_preview')
    list_editable = ('order',)
    search_fields = ('title', 'content')
    ordering = ('order', 'id')
    ckeditor_fields = ('content',)
    fieldsets = (
        ('Основное', {
            'fields': ('title', 'content')
        }),
        ('Изображение', {
            'fields': ('image',)
        }),
        ('Порядок', {
            'fields': ('order',)
        }),
    )


@admin.register(PaymentInfo)
class PaymentInfoAdmin(CKEditorAdminMixin, ImagePreviewMixin, admin.ModelAdmin):
    list_display = ('title', 'order', 'image_preview')
    list_editable = ('order',)
    search_fields = ('title', 'content')
    ordering = ('order', 'id')
    ckeditor_fields = ('content',)
    fieldsets = (
        ('Основное', {
            'fields': ('title', 'content')
        }),
        ('Изображение', {
            'fields': ('image',)
        }),
        ('Порядок', {
            'fields': ('order',)
        }),
    )


@admin.register(TermsInfo)
class TermsInfoAdmin(CKEditorAdminMixin, ImagePreviewMixin, admin.ModelAdmin):
    list_display = ('title', 'order', 'image_preview')
    list_editable = ('order',)
    search_fields = ('title', 'content')
    ordering = ('order', 'id')
    ckeditor_fields = ('content',)
    fieldsets = (
        ('Основное', {
            'fields': ('title', 'content')
        }),
        ('Изображение', {
            'fields': ('image',)
        }),
        ('Порядок', {
            'fields': ('order',)
        }),
    )


@admin.register(ContentBlock)
class ContentBlockAdmin(CKEditorAdminMixin, ImagePreviewMixin, admin.ModelAdmin):
    list_display = ('title', 'block_type', 'order', 'is_active', 'image_preview')
    list_editable = ('order', 'is_active')
    list_filter = ('block_type', 'is_active')
    search_fields = ('title', 'subtitle', 'content')
    ordering = ('order', 'id')
    ckeditor_fields = ('content',)
    fieldsets = (
        ('Идентификация блока', {
            'fields': ('title', 'block_type', 'is_active')
        }),
        ('Контент', {
            'fields': ('subtitle', 'content')
        }),
        ('Изображение', {
            'fields': ('image', 'image_alt')
        }),
        ('Порядок', {
            'fields': ('order',)
        }),
    )

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Общее', {
            'fields': ('site_name', 'footer_text')
        }),
        ('Hero', {
            'fields': (
                'hero_badge',
                'hero_primary_button',
                'hero_secondary_button',
            )
        }),
        ('Названия разделов', {
            'fields': (
                'services_menu_title', 'services_section_title',
                'terms_menu_title', 'terms_section_title',
                'payment_menu_title', 'payment_section_title',
                'portfolio_menu_title',
                'delivery_menu_title', 'delivery_section_title',
                'contact_menu_title', 'contact_section_title',
            )
        }),
        ('Блок оборудования', {
            'fields': (
                'portfolio_section_title',
                'portfolio_section_subtitle',
                'portfolio_section_text',
            )
        }),
        ('Форма и CTA', {
            'fields': (
                'contact_form_title',
                'consent_text',
                'submit_button_text',
            )
        }),
        ('Модальное окно', {
            'fields': (
                'modal_title',
                'modal_submit_button_text',
            )
        }),
        ('Мессенджеры', {
            'fields': (
                'telegram_url',
                'telegram_button_text',
                'whatsapp_url',
                'whatsapp_button_text',
            )
        }),
        ('Схема прохода', {
            'fields': (
                'pickup_route_url',
                'pickup_route_button_text',
            )
        }),
        
    )

    def has_add_permission(self, request):
        if SiteSettings.objects.count() >= 1:
            return False
        return super().has_add_permission(request)