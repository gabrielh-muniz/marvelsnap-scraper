import os
from dotenv import load_dotenv
from ..drivers.driver import Driver
from ..soup.scraper import Scraper
from ..model.card import Card

load_dotenv()

driver = Driver(os.getenv('URL'))

def scraping_result() -> list[Card]:
  card_objects = []

  webpage_html = Scraper(driver.page_source, 'html.parser')
  elements = webpage_html.get_elements('a', 'class', 'simple-card')

  for element in elements:
    try:
      new_card = Card(
        element.get('data-name'),
        element.get('data-cost'),
        element.get('data-power'),
        Scraper(element.get('data-ability'), 'html.parser').text,
        element.get('data-src'),
        element.get('data-status'),
        element.get('data-source'),
        [variant.get('data-src') for variant in element.find_all('img')][1:]    
      )
      card_objects.append(new_card)
    except:
      print('Error on scraping')

  return card_objects
