from selenium import webdriver
import csv
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://best.aliexpress.com/')
browser.maximize_window()

search_box = browser.find_element(by=By.ID, value='search-key')
search_box.send_keys('iphone 14')

search_submit_button = browser.find_element(by=By.CLASS_NAME, value='search-button')
search_submit_button.click()

result_items = browser.find_elements(by=By.CSS_SELECTOR, value='.search-card-item')
print(len(result_items))

with open("result.csv", 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Title", "Price"])

    for product in result_items:    
        name = product.find_element(by=By.CLASS_NAME, value='cards--title--2rMisuY').text
        #print(name)
        price = product.find_element(by=By.CLASS_NAME, value='manhattan--price--WvaUgDY').text
        #print(price)
        csv_writer.writerow([name, price])

browser.quit()
