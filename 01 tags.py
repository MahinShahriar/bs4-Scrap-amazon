import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook , load_workbook

wb = Workbook()
ws = wb.active
ws.title = 'Products'

with open('data/amzn.html', 'r') as f:
  html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')
products = soup.css.select(".a-section.a-spacing-base")
for product in products:
  span_title = product.find('span', class_='a-size-base-plus a-color-base a-text-normal')
  span_price = product.find('span', class_='a-price-whole')
  if span_title and span_price:
    title = span_title.text.strip()
    p_img = product.a['href']
    p_link = "https://www.amazon.com"+span_title.parent['href']
    price = span_price.text.strip()
    ws.append([title, price, p_img, p_link])

wb.save('data/amzn.xlsx')