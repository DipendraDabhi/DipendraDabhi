from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class LeavePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_dashboard(self):
        # Wait until dashboard URL is loaded
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("/dashboard/index")
        )        
    
    def click_leave(self):
        # Wait for the "Leave" menu to be visible and click on it
        leave_menu = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(@class, 'oxd-main-menu-item') and .//span[text()='Leave']]")
            )
        )
        leave_menu.click()
        

    def apply_leave(self, leave_type="US - Personal", from_date="2025-06-25", to_date="2025-06-25", comment="Vacation"):
        wait = WebDriverWait(self.driver, 10)
        
        apply_tab = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@class, 'oxd-topbar-body-nav-tab-item') and normalize-space(text())='Apply']")
        )
        )
        apply_tab.click()
        time.sleep(10)  # Optional: wait for page update
        
        # Click Leave Type dropdown
        leave_dropdown = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//label[text()='Leave Type']/following::div[contains(@class, 'oxd-select-text')][1]")))
        leave_dropdown.click()

        # Select the leave type
        leave_option = wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//div[@role='listbox']//span[text()='{leave_type}']")))
        leave_option.click()

        # Enter From Date
        from_date_input = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//label[text()='From Date']/following::input[1]")))
        from_date_input.send_keys(Keys.CONTROL, 'a')
        from_date_input.send_keys(Keys.DELETE)
        from_date_input.send_keys(from_date)

        # Enter To Date
        to_date_input = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//label[text()='To Date']/following::input[1]")))
        to_date_input.send_keys(Keys.CONTROL, 'a')
        to_date_input.send_keys(Keys.DELETE)
        to_date_input.send_keys(to_date)

        # Enter Comment
        comment_box = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//label[text()='Comments']/following::textarea")))
        comment_box.clear()
        comment_box.send_keys(comment)

        # Click Apply button
        apply_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Apply']")))
        apply_btn.click()
        print("Leave applied successfully.")
        # Optional: wait for confirmation message   
        time.sleep(5)


    def cancel_leave(self, leave_type="US - Personal", from_date="2025-06-25", to_date="2025-06-25"):
        wait = WebDriverWait(self.driver, 10)

        # Step 1: Click "My Leave" tab
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='My Leave']"))).click()
        time.sleep(5)

        # Enter From Date
        from_date_input = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//label[text()='From Date']/following::input[1]")))
        from_date_input.send_keys(Keys.CONTROL, 'a')
        from_date_input.send_keys(Keys.DELETE)
        from_date_input.send_keys(from_date)

        # Enter To Date
        to_date_input = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//label[text()='To Date']/following::input[1]")))
        to_date_input.send_keys(Keys.CONTROL, 'a')
        to_date_input.send_keys(Keys.DELETE)
        to_date_input.send_keys(to_date)

        # Click Leave Type dropdown
        leave_dropdown = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//label[text()='Leave Type']/following::div[contains(@class, 'oxd-select-text')][1]"
        )))
        leave_dropdown.click()

        # Select the leave type
        leave_option = wait.until(EC.element_to_be_clickable((
            By.XPATH, f"//div[@role='listbox']//span[normalize-space(text())='{leave_type}']"
        )))
        leave_option.click()

        # Click the Search button
        search_button = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[normalize-space()='Search']"
        )))
        search_button.click()
        time.sleep(10)

        # Locate the row with "Pending Approval" status and click the Cancel button
        pending_row_cancel_button = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//div[@role='row' and .//div[contains(text(),'Pending Approval')]]//button[normalize-space()='Cancel']"
        )))
        pending_row_cancel_button.click()
        
        print("Leave cancellation successfully.")
        # Optional: wait for confirmation message   
        time.sleep(5)