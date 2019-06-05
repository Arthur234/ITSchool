from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomerUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomerUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomerUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'age', 'is_staff']


admin.site.register(CustomUser, CustomerUserAdmin)
