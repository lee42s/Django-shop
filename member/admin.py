from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from member.models import User
# admin 수정을 위해서 admin.ModelAdmin을 상속받는 클래스를 만든다.

admin.site.register(User,)
