from django.contrib import admin
from .models import Service, Portfolio, ContactInfo, Order

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):  # Было ModelName, стало ModelAdmin
    list_display = ('title', 'price', 'order')
    list_editable = ('order',)

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