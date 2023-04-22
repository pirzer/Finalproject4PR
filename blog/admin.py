from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


# Adding action = ['cancel_event', 'schedule_event']
# Adding def cancel_event(self, request, queryset): line 19-22
# Adding def schedule_event(self, request, queryset): line 24-27
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    # actions = ['cancel_event', 'schedule_event']

    # def cancel_event(self, request, queryset):
    #     '''Adds the function Cancel Event to possible actions in
    #     the admin area'''
    #     queryset.update(status=2)

    # def schedule_event(self, request, queryset):
    #     '''Adds the function Schedule Event to possible actions in
    #     the admin area'''
    #     queryset.update(status=1)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

# Register your models here.
