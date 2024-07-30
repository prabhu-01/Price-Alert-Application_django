from django.contrib import admin
from .models import Alert

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('user', 'cryptocurrency', 'target_price', 'current_price', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'user')
    search_fields = ('user__username', 'cryptocurrency')
