from django.contrib import admin
from .models import Member, Office
from django.contrib.auth.admin import UserAdmin

members = [Office]


class UserAdminConfig(UserAdmin):
    model = Member
    search_fields = ('email', 'user_name', 'first_name',)
    list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')
    ordering = ('email',)
    list_display = ('email', 'user_name', 'first_name', 'title',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'title', 'office',
         'first_name', 'last_name', 'phone', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    # formfield_overrides = {
    #     NewUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    # }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'phone', 'title', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(members)
admin.site.register(Member, UserAdminConfig)
