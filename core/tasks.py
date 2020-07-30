from celery import shared_task, task
from core.scrapers import scrape


@task
def scrape_dev_to():
    URL = "https://dev.to/search?q=django"
    scrape(URL)
    return

