from django.contrib import admin
from .models import Service, Portfolio, ContactInfo, Order
from .models import DeliveryInfo, PaymentInfo, TermsInfo
from django.utils.html import format_html

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'order', 'image_preview')
    list_editable = ('order',)
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />', obj.image.url)
        return 'Нет фото'
    image_preview.short_description = 'Превью'

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):  # Было ModelName, стало ModelAdmin
    list_display = ('title', 'category', 'order')
    list_editable = ('order',)

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):  # Было ModelName, стало ModelAdmin
    def has_add_permission(self, request):
        if ContactInfo.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):  # Было ModelName, стало ModelAdmin
    list_display = ('name', 'phone', 'created_at', 'is_processed')
    list_editable = ('is_processed',)
    readonly_fields = ('created_at',)

@admin.register(DeliveryInfo)
class DeliveryInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)

@admin.register(PaymentInfo)
class PaymentInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)

@admin.register(TermsInfo)
class TermsInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)