from django.contrib import admin
from .models import Item, Order, OrderItem  

# Admin customization for Item model
class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}  
    list_display = [
        'title',
        'price',
        'discount',  
    ]


admin.site.register(Item, ItemAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
