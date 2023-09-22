import time

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger



"""Корзина"""
class Cart_page(Base):

    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.driver = driver


    """Locators"""

    proceed_to_checkout = "//a[@data-entity='basket-checkout-button']"




    """Getters"""

    def get_proceed_to_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.proceed_to_checkout)))





    """Actions"""

    def click_proceed_to_checkout(self):
        self.get_proceed_to_checkout().click()
        print("Click Proceed to Checkout")





    """Methods"""

    """Выбор кнопки 'Перейти к оформлению'"""
    def select_proceed_to_checkout(self):
        with allure.step("Select Proceed to Checkout"):
            Logger.add_start_step(method='select_proceed_to_checkout')
            self.driver.execute_script("window.scrollTo(0, 200)")
            self.click_proceed_to_checkout()
            Logger.add_end_step(url=self.driver.current_url, method='select_proceed_to_checkout')



