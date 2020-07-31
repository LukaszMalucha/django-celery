python manage.py migrate
python manage.py makesuper
gunicorn news_scraper.wsgi --bind=0.0.0.0:80