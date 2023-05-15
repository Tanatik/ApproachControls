from selenium.webdriver.common.by import By


class UploadPage:
    def __init__(self, driver):
        self.driver = driver

    # Web elements in this page
    def get_upload_input(self):
        upload_input = self.driver.find_element(By.ID, "upfile_0")
        return upload_input

    def get_read_terms_of_use_checkbox(self):
        read_terms_of_use_checkbox = self.driver.find_element(By.ID, "readTermsOfUse")
        return read_terms_of_use_checkbox

    def get_submit_button(self):
        submit_button = self.driver.find_element(By.NAME, "upload_button")
        return submit_button

    def get_top_message(self):
        top_message = self.driver.find_element(By.ID, "TopMessage")
        return top_message
