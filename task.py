from RPA.Browser.Selenium import Selenium
import time
from RPA.Tables import Tables
import csv

browser = Selenium()

products = []

CSV = 'output/apple.csv'

def open_browser():
    browser.open_available_browser('https://www.apple.com/')


def open_url(index):    
    browser.click_element('//html/body/nav[1]/div/ul[2]/li[' + str(index) + ']/a')


def apple(products):
    len_items = len(browser.find_elements('//html/body/nav[2]/div/ul/li'))
    for index in range(len_items):
        title_mac_book_air = browser.get_text('//html/body/nav[2]/div/ul/li[' + str(index + 1) + ']/a/span')
        link_mac_book_air = browser.get_element_attribute('//html/body/nav[2]/div/ul/li[' + str(index + 1) + ']/a', 'href')

        products.append(
            {
                'Product Apple': title_mac_book_air,
                'Link': link_mac_book_air
            }
        )

# def create_table():
#     table = Tables()
#     table_products = table.create_table(products)
#     print(table_products)


def csv_file(products, CSV):
    with open(CSV, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Apple product', 'Link'])
        for product in products:
            writer.writerow([product['Product Apple'], product['Link']])
    

if __name__ == "__main__":
    open_browser()
    products = []
    for category in range(2, 7):
        open_url(category)
        time.sleep(1)
        apple(products)
    # create_table()
    csv_file(products, CSV)    