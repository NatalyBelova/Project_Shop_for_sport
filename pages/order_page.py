import time

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger



"""Страница оформления заказа"""
class Order_page(Base):

    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.driver = driver


    """Locators"""

    name = "//input[@id='soa-property-32']"
    phone_number = "//input[@id='soa-property-3']"
    address = "//textarea[@id='soa-property-7']"




    """Getters"""

    def get_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name)))

    def get_phone_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.address)))




    """Actions"""

    def input_name(self, name):
        self.get_name().send_keys(name)
        print("Input Name")

    def input_phone_number(self, phone_number):
        self.get_phone_number().send_keys(phone_number)
        print("Input Phone number")

    def input_address(self, address):
        self.get_address().send_keys(address)
        print("Input Address")




    """Methods"""

    """Оформление заказа. Заполнение полей имя и телефон"""
    def make_order(self):
        with allure.step("Make Order"):
            Logger.add_start_step(method='make_order')
            self.input_name("Ivan")
            self.input_phone_number("89117658947")
            self.input_address("Moscow, Red Square")
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='make_order')



