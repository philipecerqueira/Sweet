from django.contrib import admin
from django.contrib.auth import admin as adminAuthDjango

from .forms import UserChangeForm, UserCreationForm
from .models import Account


@admin.register(Account)
class AccountAdmin(adminAuthDjango.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    models = Account
    fieldsets  = adminAuthDjango.UserAdmin.fieldsets + (
        ('Job', {'fields': ('job',)}),
    )