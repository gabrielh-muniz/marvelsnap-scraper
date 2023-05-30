import bs4

class Scraper(bs4.BeautifulSoup):
  def __init__(self, markup: str, parser: str) -> None:
    super(Scraper, self).__init__(markup, parser)

  def get_elements(self, tag_name: str, attr: str, attr_value: str) -> bs4.element.ResultSet:
    return self.find_all(tag_name, { attr: attr_value })

