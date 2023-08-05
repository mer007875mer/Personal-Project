# from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from jdatetime import datetime, date
from django.db import IntegrityError

class ScrapedApartmentsView(ListView):
    model = Post
    template_name = 'Main/home.html'
    context_object_name = 'apartments'
    ordering = ['-date']

    def get_queryset(self):
        return self.model.objects.all()

def get_apartment_date(date_string):
    date_parts = date_string.split('،')
    date_parts = date_parts[0].split(' ')
    num = date_parts[0]
    label = date_parts[1]
    today = datetime.now()

    if label == "روز":
        return today - timedelta(days=int(num))
    elif label == "هفته":
        return today - timedelta(weeks=int(num))
    elif label == "ماه":
        return today - timedelta(months=int(num))
    else:
        return today


def scrape_and_save_apartments(url):
    response = requests.get(url)
    page = BeautifulSoup(response.text, "html.parser")

    if response.status_code == 200:
        apartment_elements = page.find_all("div", {"class": "post-card-item-af972 kt-col-6-bee95 kt-col-xxl-4-e9d46"})

        for apartment in apartment_elements:
            link = apartment.find('a')

            if link is not None:
                href = link.get('href')
                apartment_url = f"https://divar.ir{href}"
                apartment_response = requests.get(apartment_url)
                apartment_page = BeautifulSoup(apartment_response.text, "html.parser")

                apartment_image = apartment_page.find("img", {"kt-image-block__image"})

                if apartment_image is not None:
                    image_url = apartment_image.get('src')
                    apartment_detail_element = apartment_page.find("div", {
                        "class": "kt-page-title__subtitle kt-page-title__subtitle--responsive-sized"})

                    if apartment_detail_element:
                        apartment_detail = apartment_detail_element.text
                        apartment_title = apartment_page.find("div", {
                            "class": "kt-page-title__title kt-page-title__title--responsive-sized"
                        })
                        apartment_price_element = apartment_page.find("div", {
                            "class": "kt-base-row__end kt-unexpandable-row__value-box"})
                        apartment_price = apartment_price_element.text if apartment_price_element is not None else None

                        apartment_date = get_apartment_date(apartment_detail)
                        gregorian_date = date(apartment_date.year, apartment_date.month, apartment_date.day)
                        persian_date = date.fromgregorian(date=gregorian_date)

                        today = datetime.now()
                        if apartment_date.day == today.day and apartment_date.year == today.year and apartment_date.month == today.month:

                            try:
                                print(apartment_title.text)
                                apartments_data = {
                                    'title': apartment_title.text,
                                    'price': apartment_price,
                                    'date_day': apartment_date.day,
                                    'date_month': apartment_date.month,
                                    'date_year': apartment_date.year,
                                    'buy_url': apartment_url,
                                    'image_src': image_url
                                }
                                post = Post(**apartments_data)
                                post.save()
                            except IntegrityError:
                                print("This Value is Already saved")

                    else:
                        print("Apartment detail not found.")
                        print("________________________")
                else:
                    print("Apartment image not found.")
    else:
        print(f"Request failed: {response.status_code}")
