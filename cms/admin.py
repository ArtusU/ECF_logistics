from django.contrib import admin
from .models import *

admin.site.register(Referrer)
admin.site.register(Recipient)
admin.site.register(Product)
admin.site.register(Delivery_Address)
admin.site.register(ProductCategory)
admin.site.register(Order)