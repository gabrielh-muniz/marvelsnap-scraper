import os
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()

class DriverOptions(webdriver.FirefoxOptions):
  def __init__(self, binary_path: str=os.getenv('BINARY_PATH')) -> None:
    super(DriverOptions, self).__init__()
    self.binary = binary_path
    self.add_argument('start-maximized')
    self.add_argument('--headless')
    self.add_argument('--disable-extensions')

class DriverService(webdriver.firefox.service.Service):
  def __init__(self, driver_path: str) -> None:
    super(DriverService, self).__init__()

class Driver(webdriver.Firefox):
  def __init__(self, url,  driver_path: str=os.getenv('DRIVER_PATH')):
    super(Driver, self).__init__(options=DriverOptions(), service=DriverService(driver_path))
    self.get(url)

