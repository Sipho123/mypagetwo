from django.contrib import admin

from .models import *

admin.site.register(Admin)
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(ProductImage)

