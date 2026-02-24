from django.contrib import admin
from .models import Resume, Experience, Education, Skill

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'full_name', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'full_name', 'email')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = [
        ('Informations personnelles', {
            'fields': ['full_name', 'email', 'phone']
        }),
        ('CV', {
            'fields': ['title', 'summary']
        }),
        ('Métadonnées', {
            'fields': ['created_at', 'updated_at'],
            'classes': ['collapse']
        }),
    ]

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'resume', 'current')
    list_filter = ('current', 'company')
    search_fields = ('company', 'position')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'resume', 'current')
    list_filter = ('current', 'institution')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'resume', 'proficiency')
    list_filter = ('proficiency',)