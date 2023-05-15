import os
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.pages.UploadPage import UploadPage

# Path to the file you want to upload
file_path = os.path.abspath(str(Path("../../testFiles/testImg.png")))

# URL of the web application
url = "http://www.fileconvoy.com"

# Path to your browser driver (e.g., chromedriver, geckodriver)
driver_path = ""

# Configure the browser driver (e.g., Chrome)
options = webdriver.ChromeOptions()
# Add any additional options if required

# Initialize the browser driver
# driver = webdriver.Chrome(executable_path=driver_path, options=options)
driver = webdriver.Chrome()
driver.implicitly_wait(10)

# Web elements in this page
upload_page = UploadPage(driver)

# Navigate to the web application
driver.get(url)

try:
    # Find the file input element
    file_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "upfile_0")))

    # Send the file path to the file input element
    print("Try to upload file: " + file_path)
    upload_page.get_upload_input().send_keys(file_path)
    upload_page.get_read_terms_of_use_checkbox().click()
    upload_page.get_submit_button().submit()

    assert "Your file(s) have been successfully uploaded." == upload_page.get_top_message().text

finally:
    # Quit the browser
    driver.quit()
