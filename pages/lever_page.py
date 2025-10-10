from utils.page import Page
from locators.lever_locators import LeverLocators


class LeverPage(Page):
    def is_lever_page_opened(self):
        validations = [
            self.xpath(LeverLocators.LISTED_JOB_ITEM_POSITION),
            self.xpath(LeverLocators.LISTED_JOB_ITEM_LOCATION),
            self.xpath(LeverLocators.LISTED_JOB_ITEM_DEPARTMENT),
            self.xpath(LeverLocators.APPLY_FOR_THIS_JOB_BUTTON)]
        return (self.is_open(validation) for validation in validations)

    def check_lever_url(self):
        return self.check_address("jobs.lever.co/useinsider")