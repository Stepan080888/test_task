from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
class Searchhelper:
    def __init__(self, app):
        self.app = app


    def click_search_button(self):
        wd = self.app.wd
        wd.find_element_by_id('search-submit').click()

    def fill_in_car(self, car):
        wd = self.app.wd
        self.app.open_olx_page()
        wd.find_element_by_id('headerSearch').click()
        wd.find_element_by_id('headerSearch').clear()
        wd.find_element_by_id('headerSearch').send_keys(car, Keys.ENTER)
        WebDriverWait(wd, 10).until(lambda wd: wd.find_element_by_class_name('highlight-close')).click()

    def fill_in_city_and_press_search(self, region, city):
        wd = self.app.wd
        wd.find_element_by_id('cityField').click()
        wd.find_element_by_link_text(region).click()
        wd.find_element_by_link_text(city).click()
        self.click_search_button()

    def select_money(self, money):
        wd = self.app.wd
        wait = WebDriverWait(wd, 5000)
        time.sleep(2)
        dolar = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, money)))
        dolar.click()

    def select_sorting(self, sort_param):
        wd = self.app.wd
        wait = WebDriverWait(wd, 5000)
        time.sleep(2)
        sort = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, sort_param)))
        sort.click()

    def configure_search(self, money, sort_param):
        self.select_money(money)
        self.select_sorting(sort_param)

    def get_location_from_first_item_ordinary_list(self):
        wd = self.app.wd
        first_auto = wd.find_element_by_id('offers_table').find_elements_by_class_name('offer ')[0]
        return first_auto.find_elements_by_class_name('breadcrumb')[1].text.rsplit(',', 1)[0]






