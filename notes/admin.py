from django.contrib import admin
from . import models

@admin.register(models.Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
