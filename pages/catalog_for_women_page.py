import time

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger



"""Каталог для женщин"""
class Catalog_women_page(Base):

    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.driver = driver


    """Locators"""

    logo_button = "//div[@class='header__logo']"


    """Getters"""

    def get_logo_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.logo_button)))



    """Actions"""

    def click_logo_button(self):
        self.get_logo_button().click()
        print("Click Logo button")




    """Methods"""

    """Нажатие на логотип. Ожидание: переход на главную страницу"""
    def click_logo(self):
        with allure.step("Click Logo"):
            Logger.add_start_step(method='click_logo')
            self.click_logo_button()
            time.sleep(2)
            self.assert_url("https://sportpoint.ru/")
            Logger.add_end_step(url=self.driver.current_url, method='click_logo')






