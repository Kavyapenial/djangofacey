from django.contrib import admin

from .models import Branch, Batch, Semester, Subject

# Register your models here.


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('code', 'name',)
    ordering = ('name',)
    search_fields = ('name',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_code','subject', 'teacher', 'branch',
                    'sem', 'credit',)
    ordering = ('subject',)
    search_fields = ('subject', 'teacher__name', 'subject_code',)
    list_filter = ('branch','teacher', 'sem', 'credit', )
    

@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('year', 'branch',)
    ordering = ('year',)
    search_fields = ('branch',)


@admin.register(Semester)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    search_fields = ('name',)

