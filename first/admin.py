from django.contrib import admin
from first.models import Post,  Comment

# admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
 list_display = ('title', 'slug', 'author', 'publish', 'status')
 list_filter = ('status', 'created', 'publish', 'author')
 search_fields = ('title', 'body')
 prepopulated_fields = {'slug': ('title',)}
 raw_id_fields = ('author',)
 date_hierarchy = 'publish'
 ordering = ('status', 'publish')
#  list_display = ("__all__") # this will not work like in forms.
# This will not work

# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')

