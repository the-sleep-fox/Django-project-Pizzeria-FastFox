from django.contrib import admin

from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'total_price', 'comment')
    list_filter = ('created_at',)
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
