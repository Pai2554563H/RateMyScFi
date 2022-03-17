from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.views import get_user_model

from user.models import UserProfile


# Register your models here.


admin.site.register(UserProfile)


@admin.register(get_user_model())
class UserModelAdmin(UserAdmin):
    pass
