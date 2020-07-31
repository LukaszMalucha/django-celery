
celery -A news_scraper worker --beat --scheduler django_celery_beat.schedulers.DatabaseScheduler -l info
