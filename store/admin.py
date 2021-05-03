from django.contrib import admin
from.models import Product

# Register your models here.

#slug jate automatic product_name likher sathe sathei database e add hoye jay! tar jonne nicher class ti use kora lagbe!

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','stock','category','modified_date','is_available')
    prepopulated_fields = {'slug':('product_name',)}


admin.site.register(Product,ProductAdmin)
