from celery import shared_task
from .views import scrape_and_save_apartments


@shared_task
def scrape_apartments():
    url = "https://divar.ir/s/tehran/buy-residential/jamalzadeh?size=65-100&sort=sort_date"
    scrape_and_save_apartments(url)