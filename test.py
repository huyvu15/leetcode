import selenium.webdriver as webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import os
# Import thư viện khác

import time
import requests
import pickle
import datetime
import calendar
# from selenium.webdriver.common.alert import Alert


# user_agent khác nhau của mỗi máy và trình duyệt
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.54'
edge_driver_path = os.path.join(os.getcwd(), 'msedgedriver.exe')
edge_service = Service(edge_driver_path)
edge_options = Options()
edge_options.add_argument(f'user-agent={user_agent}')
# Tạo
driver = webdriver.Edge(service=edge_service, options=edge_options)
url = 'https://shopee.vn/buyer/login?next=https%3A%2F%2Fshopee.vn%2F'

url1 = 'https://shopee.vn/'

# Lấy link
driver.get(url)

time.sleep(50)

user_name = ''


