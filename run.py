from src.utils.services import scraping_result

cards = scraping_result()

for card in cards:
  print(card)
