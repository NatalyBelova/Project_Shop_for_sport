import time

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger



"""Каталог для мужчин"""
class Catalog_men_page(Base):

    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.driver = driver


    """Locators"""

    sneakers_new_balance = "//div[@data-id='242523']"
    choose_size_sneakers_new_balance = "//div[@aria-label='3 / 10']"
    add_to_cart_sneakers_new_balance = "//button[@id='bx_117848907_242523_buy_link']"
    go_to_cart = "//a[@class='link-red__link modal-cart-links__link']"

    filter_category = "//button[@data-modal-id='#modal-586']"
    clothes = "//*[@id='modal-586']/div/div/div[2]/label/span"
    filter_product_type = "//button[@data-modal-id='#modal-587']"
    sports_suits = "//*[@id='modal-587']/div/div/div[19]/label/span/span"
    filter_brand = "//button[@data-modal-id='#modal-207']"
    nike = "//*[@id='modal-207']/div/div/div[1]/label/span/span"
    apply_filters = "//*[@id='comp_abcbbfa7b5c0833d807d0e2ca81f71fc']/section[2]/div/div[3]/button[1]"
    sports_suit_NikeM = "//*[@id='bx_3966226736_229652_7e1b8e3524755c391129a9d7e6f2d206']/div[1]/a/span[8]/span"
    choose_size_sports_suit_NikeM = "//*[@id='sizesSlider']/div[2]/label/span"
    add_to_cart_sports_suit_NikeM = "//button[@id='bx_117848907_229652_buy_link']"
    go_to_cart1 = "//a[@class='link-red__link modal-cart-links__link']"





    """Getters"""

    def get_sneakers_new_balance(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sneakers_new_balance)))

    def get_choose_size_sneakers_new_balance(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.choose_size_sneakers_new_balance)))

    def get_add_to_cart_sneakers_new_balance(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_sneakers_new_balance)))

    def get_go_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart)))

    def get_filter_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_category)))

    def get_clothes(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.clothes)))

    def get_filter_product_type(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_product_type)))

    def get_sports_suits(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sports_suits)))

    def get_filter_brand(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_brand)))

    def get_nike(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.nike)))

    def get_apply_filters(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.apply_filters)))

    def get_sports_suit_NikeM(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sports_suit_NikeM)))

    def get_choose_size_sports_suit_NikeM(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.choose_size_sports_suit_NikeM)))

    def get_add_to_cart_sports_suit_NikeM(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_sports_suit_NikeM)))

    def get_go_to_cart1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart1)))




    """Actions"""

    def click_sneakers_new_balance(self):
        self.get_sneakers_new_balance().click()
        print("Click Sneakers New Balance")

    def click_choose_size_sneakers_new_balance(self):
        self.get_choose_size_sneakers_new_balance().click()
        print("Click Choose Size Sneakers New Balancee")

    def click_add_to_cart_sneakers_new_balance(self):
        self.get_add_to_cart_sneakers_new_balance().click()
        print("Click Add to cart Sneakers New Balance")

    def click_go_to_cart(self):
        self.get_go_to_cart().click()
        print("Click Go to Cart")

    def click_filter_category(self):
        self.get_filter_category().click()
        print("Click Filter Category")

    def click_clothes(self):
        self.get_clothes().click()
        print("Click Clothes")

    def click_filter_product_type(self):
        self.get_filter_product_type().click()
        print("Click filter Product Type")

    def click_sports_suits(self):
        self.get_sports_suits().click()
        print("Click Sports suits")

    def click_filter_brand(self):
        self.get_filter_brand().click()
        print("Click filter Brand")

    def click_nike(self):
        self.get_nike().click()
        print("Click Nike")

    def click_apply_filters(self):
        self.get_apply_filters().click()
        print("Click Apply filters")

    def click_sports_suit_NikeM(self):
        self.get_sports_suit_NikeM().click()
        print("Click Sports suit Nike M")

    def click_choose_size_sports_suit_NikeM(self):
        self.get_choose_size_sports_suit_NikeM().click()
        print("Click Choose size sports suit Nike M")

    def click_add_to_cart_sports_suit_NikeM(self):
        self.get_add_to_cart_sports_suit_NikeM().click()
        print("Click Add to cart sports suit Nike M")

    def click_go_to_cart1(self):
        self.get_go_to_cart1().click()
        print("Click Go to cart1")




    """Methods"""

    """Кладем в корзину один товар"""
    def select_product(self):
        with allure.step("Select Product"):
            Logger.add_start_step(method='select_product')
            self.driver.execute_script("window.scrollTo(0, 200)")
            self.click_sneakers_new_balance()
            self.get_screenshot()
            self.click_choose_size_sneakers_new_balance()
            self.click_add_to_cart_sneakers_new_balance()
            self.click_go_to_cart()
            Logger.add_end_step(url=self.driver.current_url, method='select_product')


    """Кладем в корзину один товар с использованием фильтров"""
    def select_product_with_filters(self):
        with allure.step("Select Product with filters"):
            Logger.add_start_step(method='select_product_with_filters')
            self.driver.execute_script("window.scrollTo(0, 200)")
            self.click_filter_category()
            self.click_clothes()
            time.sleep(3)
            self.click_filter_product_type()
            self.click_sports_suits()
            time.sleep(3)
            self.click_filter_brand()
            self.click_nike()
            time.sleep(3)
            self.click_apply_filters()
            self.get_screenshot()
            time.sleep(5)
            self.click_sports_suit_NikeM()
            self.click_choose_size_sports_suit_NikeM()
            self.click_add_to_cart_sports_suit_NikeM()
            self.click_go_to_cart1()
            Logger.add_end_step(url=self.driver.current_url, method='select_product_with_filters')






