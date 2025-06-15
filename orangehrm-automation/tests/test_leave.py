import time
from pages.login_page import LoginPage
from pages.leave_page import LeavePage
from utils.base_test import BaseTest

class TestLeave(BaseTest):

    def test_apply_and_cancel_leave(self):
        login_page = LoginPage(self.driver)
        login_page.login("Admin", "admin123")

        leave_page = LeavePage(self.driver)
        leave_page.navigate_to_dashboard()
        leave_page.click_leave()
        leave_page.apply_leave(
            leave_type="US - Personal",
            from_date="2025-06-27",
            to_date="2025-06-27",
            comment="Vacation"
        )
        leave_page.cancel_leave(
            leave_type="US - Personal",
            from_date="2025-06-27",
            to_date="2025-06-27")
        