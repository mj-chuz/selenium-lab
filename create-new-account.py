import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class MagentoDemoTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)  

    def test_1_create_account(self):
        self.driver.get("https://magento.softwaretestingboard.com/")

        sign_in_link = self.driver.find_element(By.LINK_TEXT, "Create an Account")
        sign_in_link.click()

        create_account_form1 = self.driver.find_elements(By.ID, "form-validate")
        create_account_form = create_account_form1[0]
        first_name_input = create_account_form.find_element(By.ID, "firstname")
        first_name_input.send_keys("Maria")
        last_name_input = create_account_form.find_element(By.ID, "lastname")
        last_name_input.send_keys("Vargas")
        email_input = create_account_form.find_element(By.ID, "email_address")
        email_input.send_keys("mariajesusvargas30@example.com")
        password_input = create_account_form.find_element(By.ID, "password")
        password_input.send_keys("Password123.123")
        confirm_password_input = create_account_form.find_element(By.ID, "password-confirmation")
        confirm_password_input.send_keys("Password123.123")
        create_account_button = create_account_form.find_element(By.XPATH, "//button[@title='Create an Account']")
        create_account_button.click()

        time.sleep(2)

        welcome_message = self.driver.find_element(By.XPATH, "//*[@id='maincontent']/div[1]/div[2]/div/div/div")
        self.assertEqual(welcome_message.text, "Thank you for registering with Main Website Store.")

        self.driver.get("https://magento.softwaretestingboard.com/customer/account/logout/%22")

        sign_in_link_again = self.driver.find_element(By.LINK_TEXT, "Sign In")
        self.assertIsNotNone(sign_in_link_again)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()