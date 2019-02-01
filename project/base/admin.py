from django.contrib import admin
from django.contrib.auth.models import User

from base.models import UserAdmin

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
