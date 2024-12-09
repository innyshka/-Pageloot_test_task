from django.contrib import admin
from users.models import User, Expense


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = 'username', 'email',
    search_fields = 'username', 'email',


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = 'user__username', 'title', 'amount', 'date', 'category',
    search_fields = 'user__username', 'user__email', 'title',
    list_filter = 'user', 'date', 'category',
    autocomplete_fields = 'user',
    fieldsets = (
        ('Main', {
            'fields': ('user', 'title', 'amount', 'date', 'category')
        }),
    )
