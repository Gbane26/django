from django.contrib import admin

# Register your models here.

from . models import Project
from . models import Project_detail

# admin.site.register(Project)
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'tecnology', 'image')
    list_filter = ('title',)
    search_fields = ('title',)


@admin.register(Project_detail)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'tecnology', 'image', 'Project_id')
    
        