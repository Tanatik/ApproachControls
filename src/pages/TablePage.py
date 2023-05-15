from selenium.webdriver.common.by import By


class TablePage:
    def __init__(self, driver):
        self.driver = driver

    # Web elements in this page
    def get_table_column(self, num_of_column):
        upload_input = self.driver.find_element(By.CSS_SELECTOR, "#customers td:nth-child(" + num_of_column + ")")
        return upload_input

    def get_tabel_column_title(self):
        read_terms_of_use_checkbox = self.driver.find_elements(By.CSS_SELECTOR, "#customers tr th")
        return read_terms_of_use_checkbox
