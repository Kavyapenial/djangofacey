from django.contrib import admin

# Register your models here.
from .models import Attendance, Student, AttendanceCaptureProof


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('subject', 'student', 'date', 'hour', 'is_present',)
    ordering = ('date',)
    search_fields = ('subject', 'date',)
    list_filter = ('subject','student', 'date', )


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('reg_id','name','batch', 'profile',)
    ordering = ('name',)
    search_fields = ('name', 'reg_id',)
    list_filter = ('batch',)
    
@admin.register(AttendanceCaptureProof)
class AttendanceImageAdmin(admin.ModelAdmin):
    list_display = ('date','capture_image',)
    ordering = ('date',)
    



# admin.site.register(Attendance)
# admin.site.register(Student)
# admin.site.register(Subject)
