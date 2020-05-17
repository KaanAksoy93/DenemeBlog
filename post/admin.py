from django.contrib import admin

# Register your models here.
from.models import Post # Link Post to Admin Panel

class PostAdmin(admin.ModelAdmin):

    list_display = ['title','publishingdate']
    list_filter =  ['publishingdate']
    search_fields =  ['title','content']



    class Meta:

        model=Post



admin.site.register(Post,PostAdmin)
