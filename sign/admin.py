from django.contrib import admin
from sign.models import Event, Guest


# 注册models
# admin.site.register(Event)
# admin.site.register(Guest)


class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'start_time', 'id']
    search_fields = ['name']  # 搜索功能
    list_filter = ['status']  # 过滤功能


class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname', 'phone', 'email', 'sign', 'create_time', 'event']
    list_display_links = ['realname', 'phone']  # 显示链接
    search_fields = ['realname', 'phone']  # 搜索功能
    list_filter = ['sign']  # 过滤功能


admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)
