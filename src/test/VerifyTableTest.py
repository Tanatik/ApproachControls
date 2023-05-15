from selenium import webdriver

from src.pages.TablePage import TablePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


url = "https://www.w3schools.com/html/html_tables.asp"

options = webdriver.ChromeOptions()
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(url)

table_page = TablePage(driver)

try:
    file_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "customers")))

    assert len(table_page.get_tabel_column_title()) == 3
    assert "Company" == table_page.get_tabel_column_title()[0].text
    assert "Contact" == table_page.get_tabel_column_title()[1].text
    assert "Country" == table_page.get_tabel_column_title()[2].text

finally:
    # Quit the browser
    driver.quit()
