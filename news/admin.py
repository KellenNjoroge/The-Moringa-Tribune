from django.contrib import admin
from . models import Editor,Article,Tags


class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('Tags')


admin.site.register(Editor)
admin.site.register(Article)
admin.site.register(Tags)
