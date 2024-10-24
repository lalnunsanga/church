from django.contrib import admin
from . models import Post, Comment, Category, Record
from .models import Staff  

admin.site.register(Staff)  
# Register your models here.
admin.site.site_header = ('Office Administration')

admin.site.register(Post)
admin.site.register(Comment)
#admin.site.register(Category)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('user','title', 'author', 'date', 'category_image', 'description')
