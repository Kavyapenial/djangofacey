from django.contrib import admin

from .models import Teacher

# Register your models here.

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'email', 'user')
    ordering = ('name',)
    search_fields = ('name','email')
    fieldsets = (
        (None, {
            'fields': ('name', 'designation', 'email','pic',)
        }),
    )
    list_filter = ('designation',)