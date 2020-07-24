from django.contrib import admin
from rangefilter.filter import DateRangeFilter

# Register your models here.
from .models import Attendance, Student, AttendanceCaptureProof


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('subject', 'student', 'date', 'hour', 'is_present',)
    ordering = ('date',)
    search_fields = ( 'student__name', 'student__reg_id', 'subject__subject', 'subject__subject_code')
    list_filter = ('subject',
        ('date', DateRangeFilter),)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('reg_id','name','batch', 'profile', 'face_encodings',)
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
