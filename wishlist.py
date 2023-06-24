import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MagentoDemoTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)  
        cls.wait = WebDriverWait(cls.driver, 10)

    def test_add_and_delete_wishlist(self):
        self.driver.get("https://magento.softwaretestingboard.com/")
        
        sign_in_link = self.driver.find_element(By.LINK_TEXT, "Sign In")
        sign_in_link.click()

        email_input = self.driver.find_element(By.ID, "email")
        email_input.send_keys("mariajesusvargas9@example.com")
        password_input = self.driver.find_element(By.ID, "pass")
        password_input.send_keys("Password123.123")
        self.driver.find_element(By.ID, "send2").click()

        #Add to wishlist
        self.driver.find_element(By.XPATH, "//*[@id='maincontent']/div[3]/div/div[2]/div[3]/div/div/ol/li[1]").click()
        self.driver.find_element(By.XPATH, "//*[@id='maincontent']/div[2]/div/div[1]/div[5]/div/a[1]").click()

        wishlist_counter = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='toolbar-number']")))
        self.assertEqual(wishlist_counter.text, "1 Item")

        #delete from wishlist
        remove_link = self.driver.find_element(By.XPATH, "//a[@title='Remove This Item']")
        remove_link.click()

        empty_message = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.message.info.empty")))
        message_text = empty_message.find_element(By.TAG_NAME, "span").text
        self.assertEqual(message_text, "You have no items in your wish list.")


        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()


