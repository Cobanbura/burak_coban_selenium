from utils.page import Page
from locators.qa_locators import QALocators


class QAPage(Page):

    def open_qa_jobs_page(self):
        self.driver.get("https://useinsider.com/careers/quality-assurance/")

    def is_qa_jobs_page_opened(self):
        return self.is_open(self.xpath(QALocators.QA_PAGE_TITLE))

    def click_see_all_QA_jobs(self):
        self.click(self.xpath(QALocators.JOBS_BUTTON))

    def is_all_QA_jobs_page_opened(self):
        self.wait_f(self.xpath(QALocators.JOBS_PAGE_LANG_DROPDOWN))
        return self.is_open(self.xpath(QALocators.JOBS_PAGE_LANG_DROPDOWN))

    def scroll_to_job_lists(self):
        self.scroll_to_element(self.xpath(QALocators.BROWSE_OPEN_POSITIONS))
        self.highlight_element(self.xpath(QALocators.BROWSE_OPEN_POSITIONS))

    def apply_location_filter(self, location=""):
        self.select(self.id(QALocators.LOCATION_FILTER_DROPDOWN), location)

    def apply_department_filter(self, department=""):
        self.select(self.id(QALocators.DEPARTMENT_FILTER_DROPDOWN), department)

    def is_job_list_visible(self):
        return self.is_open(self.xpath(QALocators.JOBS_LIST))

    def check_filtered_job_list(self):
        try:
            self.wait_f(self.xpath(QALocators.LISTED_QA_JOB))
            return True
        except:
            try:
                self.wait_f(self.xpath(QALocators.NO_JOBS_AVAILABLE))
                assert False, "No jobs available."
            except:
                return False

    def check_job_list_details(self):
        print("Initialize check job list details method")
        try:
            job_count = self.get_list_count(self.xpath(QALocators.LISTED_JOB_ITEM))
            print(f"Job count is:{job_count}")
            for index in range(1, job_count + 1):
                assert self.is_open(
                    self.xpath(
                        f"({QALocators.LISTED_JOB_ITEM})[{index}]{QALocators.LISTED_JOB_ITEM_POSITION}")), "Failed to validate position."
                print("Position value of job listing is validated.")
                assert self.is_open(
                    self.xpath(
                        f"({QALocators.LISTED_JOB_ITEM})[{index}]{QALocators.LISTED_JOB_ITEM_DEPARTMENT}")), "Failed to validate department."
                print("Department value of job listing is validated.")
                assert self.is_open(
                    self.xpath(
                        f"({QALocators.LISTED_JOB_ITEM})[{index}]{QALocators.LISTED_JOB_ITEM_LOCATION}")), "Failed to validate location."
                print("Location value of job listing is validated.")
                return True
        except:
            return False

    def click_view_role_button(self):
        self.hover_on_element(self.xpath(QALocators.LISTED_JOB_ITEM))
        self.hover_on_element(self.xpath(QALocators.LISTED_JOB_ITEM_LOCATION))
        self.click(self.xpath(QALocators.LISTED_JOB_ITEM_VIEW_ROLE_BUTTON))
        self.sleep(5)