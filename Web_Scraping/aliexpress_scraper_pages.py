from selenium import webdriver
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configuration du navigateur
browser = webdriver.Firefox()
browser.get('https://best.aliexpress.com/')
browser.maximize_window()

# Recherche
search_box = browser.find_element(by=By.ID, value='search-key')
search_box.send_keys('iphone 14')
search_box.send_keys(Keys.RETURN)

# Attendre que les résultats se chargent (ajuster le délai selon les besoins)
time.sleep(5)

# Récupérer les résultats de toutes les pages
page_number = 1
max_pages = 6  # Nombre maximal de pages à parcourir (ajuster selon les besoins)

with open("results.csv", 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Titre", "Prix"])

    while page_number <= max_pages:
        result_items = browser.find_elements(by=By.CSS_SELECTOR, value='.search-card-item')
        print(len(result_items))
        for product in result_items:
            name = product.find_element(by=By.CLASS_NAME, value='manhattan--titleText--WccSjUS').text
            price = product.find_element(by=By.CLASS_NAME, value='manhattan--price--WvaUgDY').text
            csv_writer.writerow([name, price])
        
        # Passer à la page suivante
        try:
            next_page_button = browser.find_element(by=By.CLASS_NAME, value='next-next')
            next_page_button.click()
            page_number += 1
            time.sleep(5)  # Attendre que la nouvelle page se charge
        except:
            break  # Sortir de la boucle s'il n'y a plus de pages suivantes

# Fermer le navigateur
browser.quit()
