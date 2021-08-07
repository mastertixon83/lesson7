from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Модель заказа в админке"""
    list_display = [
        'pk', 'first_name', 'last_name', 'email', 'address',
        'postal_code', 'city', 'created_at', 'updated_at', 'paid'
    ]
    list_editable = ['paid', ]
    list_filter = ['paid', 'created_at', 'updated_at']
    inlines = [OrderItemInline]
