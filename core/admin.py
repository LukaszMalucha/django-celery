from django.contrib import admin
from core.models import NewsItem, ScrapeRecord


class NewsItemAdmin(admin.ModelAdmin):
    list_display = [
        'source',
        'link',
        'title',
        'created',
    ]

admin.site.register(NewsItem, NewsItemAdmin)
admin.site.register(ScrapeRecord)