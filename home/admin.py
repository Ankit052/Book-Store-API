from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["user_name","age","city","phone_number","email","created_date"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name","created_date"]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["name","author_name","category","publish_date","price","created_date"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["ordered_by","get_books","ordered_date"]
