from django.contrib import admin

from category.models import Category
from product.models import Product


admin.site.register(Product)
admin.site.register(Category)
