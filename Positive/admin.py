from django.contrib import admin
from .models import Positive
from django_summernote.admin import SummernoteModelAdmin


class PositiveAdmin(SummernoteModelAdmin):
    """
    Admin use summernote for positive story
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    summernote_fields = ('method', 'positivestory')


# Register the models
admin.site.register(Positive, PositiveAdmin)
