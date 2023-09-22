import time

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger



"""Главная страница"""
class Main_page(Base):

    url = 'https://sportpoint.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Locators"""

    for_men = "//*[@id='subMenu']/div[1]"
    for_women = "//*[@id='subMenu']/div[2]"
    for_children = "//*[@id='subMenu']/div[3]"
    kinds_of_sports = "//*[@id='subMenu']/div[4]"
    brands = "//*[@id='subMenu']/div[5]"
    search_field = "//input[@id='title-search-input']"
    accept_cookies = "//button[@class='product-data__cart cookie_accept']"
    accept_city = "//button[@class='link-red__link modal-cart-links__link js-change-location js-close-header_city_choice_confirm_window']"
    change_city ="//a[@class='header_city_choice_link modal-link']"
    city_Ekaterinburg = "//a[@data-loc-id='2243']"
    city_Krasnodar = "//a[@data-loc-id='1168']"
    city_Domodedovo = "//a[@data-loc-id='92']"
    search = "//input[@id='title-search-input']"

    how_to_buy = "//a[text()='Как купить']"
    the_shops = "//a[text()='Магазины']"
    shipping_and_payment = "//a[text()='Доставка и оплата']"
    vacancies = "//a[text()='Вакансии']"
    about_company = "//a[text()='О компании']"
    blog = "/html/body/div[3]/div/header/div[2]/div/div[2]/div[3]/a"




    """Getters"""

    def get_for_men(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.for_men)))

    def get_for_women(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.for_women)))

    def get_for_children(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.for_children)))

    def get_kinds_of_sports(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.kinds_of_sports)))

    def get_brands(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brands)))

    def get_search_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_field)))

    def get_accept_cookies(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.accept_cookies)))

    def get_accept_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.accept_city)))

    def get_change_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.change_city)))

    def get_city_Ekaterinburg(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_Ekaterinburg)))

    def get_city_Krasnodar(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_Krasnodar)))

    def get_city_Domodedovo(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_Domodedovo)))

    def get_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search)))

    def get_how_to_buy(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.how_to_buy)))

    def get_the_shops(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.the_shops)))

    def get_shipping_and_payment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shipping_and_payment)))

    def get_vacancies(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.vacancies)))

    def get_about_company(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.about_company)))

    def get_blog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.blog)))




    """Actions"""

    def click_for_men(self):
        self.get_for_men().click()
        print("Click Men")

    def click_for_women(self):
        self.get_for_women().click()
        print("Click Women")

    def click_for_children(self):
        self.get_for_children().click()
        print("Click Children")

    def click_kinds_of_sports(self):
        self.get_kinds_of_sports().click()
        print("Click Kinds of sports")

    def click_brands(self):
        self.get_brands().click()
        print("Click Brands")

    def input_search_field(self, product):
        self.get_search_field().send_keys(product)
        print("Input Search Field")

    def click_accept_cookies(self):
        self.get_accept_cookies().click()
        print("Click Accept Cookies")

    def click_accept_city(self):
        self.get_accept_city().click()
        print("Click Accept City")

    def click_change_city(self):
        self.get_change_city().click()
        print("Click Change city")

    def click_city_Ekaterinburg(self):
        self.get_city_Ekaterinburg().click()
        print("Click city Ekaterinburg")

    def click_city_Krasnodar(self):
        self.get_city_Krasnodar().click()
        print("Click city Krasnodar")

    def click_city_Domodedovo(self):
        self.get_city_Domodedovo().click()
        print("Click city Domodedovo")

    def click_search(self):
        self.get_search().click()
        print("Click Search")

    def input_search(self, product):
        self.get_search().send_keys(product)
        print("Input Search")

    def click_how_to_buy(self):
        self.get_how_to_buy().click()
        print("Click How to buy")

    def click_the_shops(self):
        self.get_the_shops().click()
        print("Click The shops")

    def click_shipping_and_payment(self):
        self.get_shipping_and_payment().click()
        print("Click Shipping and payment")

    def click_vacancies(self):
        self.get_vacancies().click()
        print("Click Vacancies")

    def click_about_company(self):
        self.get_about_company().click()
        print("Click About company")

    def click_blog(self):
        self.get_blog().click()
        print("Click Blog")




    """Methods"""

    """Выбор категории 'Мужчины'"""
    def select_men(self):
        with allure.step("Select Men"):
            Logger.add_start_step(method='select_men')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_accept_cookies()
            self.click_accept_city()
            time.sleep(2)
            self.click_for_men()
            Logger.add_end_step(url=self.driver.current_url, method='select_men')


    """Выбор категории 'Женщины'"""
    def select_women(self):
        with allure.step("Select Women"):
            Logger.add_start_step(method='select_women')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_accept_cookies()
            self.click_accept_city()
            time.sleep(3)
            self.click_for_women()
            Logger.add_end_step(url=self.driver.current_url, method='select_women')


    """Выбор категории 'Детям'"""
    def select_children(self):
        with allure.step("Select Children"):
            Logger.add_start_step(method='select_children')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_accept_cookies()
            self.click_accept_city()
            self.click_for_children()
            Logger.add_end_step(url=self.driver.current_url, method='select_children')


    """Выбор категории 'Виды спорта'"""
    def select_kinds_of_sports(self):
        with allure.step("Select Kinds of sport"):
            Logger.add_start_step(method='select_kinds_of_sports')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_accept_cookies()
            self.click_accept_city()
            self.click_kinds_of_sports()
            Logger.add_end_step(url=self.driver.current_url, method='select_kinds_of_sports')


    """Выбор категории 'Бренды'"""
    def select_brands(self):
        with allure.step("Select Brands"):
            Logger.add_start_step(method='select_brands')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_accept_cookies()
            self.click_accept_city()
            self.click_brands()
            Logger.add_end_step(url=self.driver.current_url, method='select_brands')


    """Смена города на Екатеринбург"""
    def change_city_Ekaterinburg(self):
        with allure.step("Change city Ekaterinburg"):
            Logger.add_start_step(method='change_city')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.click_change_city()
            self.click_city_Ekaterinburg()
            time.sleep(2)
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='change_city')


    """Смена города на Краснодар"""
    def change_city_Krasnodar(self):
        with allure.step("Change city Krasnodar"):
            Logger.add_start_step(method='change_city')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.click_change_city()
            self.click_city_Krasnodar()
            time.sleep(2)
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='change_city')


    """Смена города на Домодедово"""
    def change_city_Domodedovo(self):
        with allure.step("Change city Domodedovo"):
            Logger.add_start_step(method='change_city')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.click_change_city()
            self.click_city_Domodedovo()
            time.sleep(2)
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='change_city')


    """Метод проверки строки поиска по слову 'Кепки'"""
    def search_caps(self):
        with allure.step("Search Сaps"):
            Logger.add_start_step(method='search_caps')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.click_search()
            self.input_search("Кепки")
            self.get_search().send_keys(Keys.RETURN)
            self.driver.execute_script("window.scrollTo(0, 500)")
            time.sleep(2)
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='search_caps')


    """Метод проверки строки поиска по слову 'Аксессуары'"""
    def search_accessories(self):
        with allure.step("Search Accessories"):
            Logger.add_start_step(method='search_accessories')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.click_search()
            self.input_search("Аксессуары")
            self.get_search().send_keys(Keys.RETURN)
            self.driver.execute_script("window.scrollTo(0, 500)")
            time.sleep(2)
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='search_accessories')


    """Метод проверки строки поиска по слову 'Шарфы'"""
    def search_scarves(self):
        with allure.step("Search Scarves"):
            Logger.add_start_step(method='search_scarves')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.click_search()
            self.input_search("Шарфы")
            self.get_search().send_keys(Keys.RETURN)
            self.driver.execute_script("window.scrollTo(0, 500)")
            time.sleep(2)
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='search_scarves')


    """Выбор второстепенных пунктов меню"""
    def select_other_menu_items(self):
        with allure.step("Select Menu Items"):
            Logger.add_start_step(method='select_other_menu_items')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_accept_city()
            time.sleep(5)
            self.click_how_to_buy()
            self.get_screenshot()
            self.click_the_shops()
            self.get_screenshot()
            self.click_shipping_and_payment()
            self.get_screenshot()
            self.click_vacancies()
            self.get_screenshot()
            self.click_about_company()
            self.get_screenshot()
            self.click_blog()
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='select_other_menu_items')


