from django.contrib import admin

# Register your models here.
from .models import Attendance, Student, Subject, Batch, Branch


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('batch', 'branch',)
    ordering = ('batch',)
    search_fields = ('branch',)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('subject', 'student', 'date', 'hour', 'is_present',)
    ordering = ('date',)
    search_fields = ('subject', 'date',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('reg_id', 'branch', 'profile', 'name',)
    ordering = ('name',)
    search_fields = ('name', 'reg_id',)


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('bcode', 'bname',)
    ordering = ('bname',)
    search_fields = ('bname',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'branch', 'subject_code',
                    'sem', 'subject', 'credit',)
    ordering = ('subject',)
    search_fields = ('subject', 'subject_code',)


# admin.site.register(Attendance)
# admin.site.register(Student)
# admin.site.register(Subject)
