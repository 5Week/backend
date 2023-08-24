from django.contrib import admin
from .models import Board
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Board)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = (
        'title',
        'content',
        'writer'
    )
    list_display_links = list_display