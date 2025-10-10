from utils.page import Page
from locators.career_locators import CareerLocators


class CareerPage(Page):

    def is_career_page_opened(self):
        return self.is_open(self.xpath(CareerLocators.CAREER_PAGE))

    def is_location_visible(self):
        return self.is_open(self.xpath(CareerLocators.CAREER_LOCATION))

    def is_teams_visible(self):
        return self.is_open(self.xpath(CareerLocators.TEAMS_SECTION))

    def is_life_visible(self):
        return self.is_open(self.xpath(CareerLocators.LIFE_AT_INSIDER_SECTION))