from django.contrib import admin
from myuser.models import MyUser


class MyuserAdmin(admin.ModelAdmin):
	list_display = 'username', 'password'

admin.site.register(MyUser, MyuserAdmin)
