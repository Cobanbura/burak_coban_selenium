from utils.driver_setup import get_driver
from pages.home_page import HomePage
from pages.career_page import CareerPage
from pages.qa_page import QAPage
from pages.lever_page import LeverPage


def main():
    driver = get_driver()

    try:
        # Open home page and validate
        home_page = HomePage(driver)
        home_page.open_home_page()
        assert home_page.is_home_page_opened(), "Home page did not open correctly."
        print("Home page is validated successfully.")

        # Navigate to career page and validate career page
        home_page.click_company_menu()
        home_page.click_careers_link()
        career_page = CareerPage(driver)
        assert career_page.is_career_page_opened(), "Careers page did not open correctly."
        print("Careers page is validated successfully.")

        # Check if the career page sections are open
        assert career_page.is_location_visible(), "Locations section is not visible."
        print("Locations section is validated.")
        assert career_page.is_life_visible(), "Life section is not visible."
        print("Life section is validated.")
        assert career_page.is_teams_visible(), "Teams section is not visible."
        print("Teams section is validated.")

        # Navigate to QA jobs page and validate jobs page
        qa_page = QAPage(driver)
        qa_page.open_qa_jobs_page()
        assert qa_page.is_qa_jobs_page_opened(), "QA Jobs page did not open correctly."
        print("QA Jobs page is validated successfully.")
        qa_page.click_see_all_QA_jobs()
        print("Clicked to see all jobs button.")
        assert qa_page.is_all_QA_jobs_page_opened(), "All QA Jobs page did not open."
        print("All QA Jobs page is validated.")
        qa_page.scroll_to_job_lists()
        print("Scrolled to Browse Open Positions header.")
        qa_page.apply_location_filter(location="Istanbul, Turkiye")
        print("QA Jobs page location filter is applied.")
        qa_page.apply_department_filter(department="Quality Assurance")
        print("QA Jobs page department filter is applied.")
        assert qa_page.is_job_list_visible(), "Job list is not visible."
        print("QA Jobs list visibility is validated.")
        assert qa_page.check_filtered_job_list(), "Job list filtering is failed."
        print("Filtered QA Jobs list is validated.")
        assert qa_page.check_job_list_details(), "QA Jobs Details cannot be validated."
        print("QA Jobs details are validated.")
        qa_page.click_view_role_button()

        # Navigate to Lever (Role) Page
        lever_page = LeverPage(driver)
        lever_page.switch_to_next_tab()
        assert lever_page.is_lever_page_opened(), "Lever Page did not open correctly."
        print("Redirected page is validated successfully.")
        assert lever_page.check_lever_url(), "Lever URL is incorrect"
        print("Lever Job Page URL is validated.")
        print("Testcase is completed successfully.")

    except AssertionError as e:
        print(str(e))
        print("Testcase is failed.")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
