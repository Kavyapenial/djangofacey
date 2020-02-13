from django.contrib.auth.models import User, Group
from django.contrib import admin

admin.site.unregister(User)
admin.site.unregister(Group)