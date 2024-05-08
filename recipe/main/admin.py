from django.contrib import admin
from.models import AdvUser, Category, Rs

class AdvUserAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    fields = (('username', 'email'), ('first_name', 'last_name'), ('send_messages', 'is_active'), ('is_staff', 'is_superuser'), 'groups', 'user_permissions', ('last_login', 'date_joined'))
    readonly_fields = ('last_login', 'date_joined')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    search_fields =('name',)
    fields = (('name', 'order'),)

class RsAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'description', 'author', 'created_at')
    fields = (('category', 'author'), ('title', 'cooking_time'), ('description', 'cooking_steps'), 'image')

admin.site.register(AdvUser, AdvUserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Rs, RsAdmin)
