class HomeLocators:
    FOOTER_COPYRIGHT = "//div[@class='footer_copyright_holder' and contains(., 'All rights reserved.')]"
    COMPANY_BUTTON = "//li[contains(@class, 'nav-item')]//a[contains(@class, 'nav-link') and contains(., 'Company')]"
    CAREERS_LINK = "//div[contains(@class,'dropdown-menu')]//a[text()='Careers']"
    HOME_LOCATOR = "//body[contains(@class, 'home')]"
