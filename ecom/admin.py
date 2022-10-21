from django.contrib import admin
from .models import Category, Customer,Product,Orders,Feedback,SizeVariant
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Customer, CustomerAdmin)

class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Orders, OrderAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    pass
admin.site.register(Feedback, FeedbackAdmin)
# Register your models here.

admin.site.register(Category)

@admin.register(SizeVariant)
class SizeVariantAdmin(admin.ModelAdmin):
    model = SizeVariant

