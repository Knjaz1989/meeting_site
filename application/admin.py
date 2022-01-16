from django.contrib import admin
from application.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
