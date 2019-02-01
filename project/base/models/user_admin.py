from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from base.models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
