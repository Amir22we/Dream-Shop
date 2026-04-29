from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Profile, Seller

# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False

# class CustomUserAdmin(UserAdmin):
#     inlines = [ProfileInline]

# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'city', 'date_of_birth', 'created']
    search_fields = ['user__username', 'phone', 'city']
    readonly_fields = ['created', 'updated']

@admin.register(Seller)
class sellerAdmin(admin.ModelAdmin):
    list_display = ['user', 'product_category', 'shop_name']