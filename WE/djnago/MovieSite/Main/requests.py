import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def get_apartment_date(date_string):
    date_parts = date_string.split('،')
    date_parts = date_parts[0].split(' ')
    num = int(date_parts[0])
    label = date_parts[1]
    today = datetime.now()

    if label == "روز":
        return today - timedelta(days=num)
    elif label == "هفته":
        return today - timedelta(weeks=num)
    elif label == "ماه":
        return today - timedelta(months=num)
    else:
        return today

def scrape_apartments(url):
    response = requests.get(url)
    page = BeautifulSoup(response.text, "html.parser")

    if response.status_code == 200:
        apartments = page.find_all("div", {"class": "post-card-item-af972 kt-col-6-bee95 kt-col-xxl-4-e9d46"})
        
        for apartment in apartments:
            link = apartment.find('a')
            href = link['href']
            apartment_url = f"https://divar.ir{href}"

            apartment_response = requests.get(apartment_url)
            apartment_page = BeautifulSoup(apartment_response.text, "html.parser")
            
            apartment_detail_element = apartment_page.find("div", {"class": "kt-page-title__subtitle kt-page-title__subtitle--responsive-sized"})
            if apartment_detail_element:
                apartment_detail = apartment_detail_element.text

                apartment_price = apartment_page.find("div", {"class": "kt-base-row__end kt-unexpandable-row__value-box"})
                apartment_price_detail = apartment_price.find("p", {"class": "kt-unexpandable-row__value"})
                apartment_date = get_apartment_date(apartment_detail)
                today = datetime.now()

                if(apartment_date.day == today.day and apartment_date.year == today.year and apartment_date.month == today.month):
                    title = apartment_detail
                    pass
                    # print(f"{apartment_detail}\n")
                    # print(f"{apartment_date.day}/{apartment_date.month}/{apartment_date.year}")
                    # print(f"apartment price: {apartment_price_detail.text}\n")
                    # print(f"buy apartment at: {apartment_url}")
                    # print("________________________")
            else:
                print("Apartment detail not found.")
                print("________________________")

    else:
        print(f"Request failed: {response.status_code}")


url = "https://divar.ir/s/tehran/buy-residential/jamalzadeh?size=90-100&sort=sort_date"
scrape_apartments(url)