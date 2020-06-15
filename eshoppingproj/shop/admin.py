from django.contrib import admin
from  shop.models import  product,contact,orders,orderupdate,EMPMODEL

# Register your models here.

class  products (admin.ModelAdmin):
    list_display = ['product_name',' desc','pub_date']

admin.site.register(product)
admin.site.register(contact)
admin.site.register(orders)
admin.site.register(orderupdate)
admin.site.register(EMPMODEL)

