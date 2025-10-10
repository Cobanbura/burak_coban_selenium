from utils.page import Page
from locators.home_locators import HomeLocators


class HomePage(Page):

    def open_home_page(self):
        self.driver.get("https://useinsider.com/")

    def is_home_page_opened(self):
        return self.is_open(self.xpath(HomeLocators.HOME_LOCATOR))

    def click_company_menu(self):
        self.click(self.xpath(HomeLocators.COMPANY_BUTTON))

    def click_careers_link(self):
        self.click(self.xpath(HomeLocators.CAREERS_LINK))