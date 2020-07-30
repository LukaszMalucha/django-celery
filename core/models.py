from django.db import models
from datetime import datetime

class NewsItem(models.Model):
    source = models.CharField(max_length=100, default="Not Specified")
    link = models.TextField()
    title = models.CharField(max_length=200, default="Not Specified")
    created = models.DateTimeField(default=datetime.today())

    def __str__(self):
        return self.link[:50]


class ScrapeRecord(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.timestamp}"