from django.contrib import admin
from shop.models import item

# Register your models here.
@admin.register(item)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','created_at',)
    list_filter = ('author',)
    search_fields = ('title',)
