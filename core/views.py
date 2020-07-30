from django.shortcuts import render
from django.views import generic
from core.models import NewsItem

class NewsItemListView(generic.ListView):
    model = NewsItem
    template_name = "news_item_list.html"