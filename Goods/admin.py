from django.contrib import admin
from .models import *


admin.site.register(Banner)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImg)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Order)