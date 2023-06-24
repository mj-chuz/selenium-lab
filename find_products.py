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

    def test_search_products(self):
        self.driver.get("https://magento.softwaretestingboard.com/")
        
        sign_in_link = self.driver.find_element(By.LINK_TEXT, "Sign In")
        sign_in_link.click()

        email_input = self.driver.find_element(By.ID, "email")
        email_input.send_keys("mariajesusvargas9@example.com")
        password_input = self.driver.find_element(By.ID, "pass")
        password_input.send_keys("Password123.123")
        self.driver.find_element(By.ID, "send2").click()

        #search for existent product
        search_input = self.driver.find_element(By.ID, "search")
        search_input.clear()
        search_input.send_keys("Radiant Tee")  
        search_button = self.driver.find_element(By.CSS_SELECTOR, ".action.search")
        search_button.click()

        search_results = self.driver.find_elements(By.CSS_SELECTOR, ".product-item")
        self.assertTrue(len(search_results) > 0, "No se encontraron resultados para la búsqueda de ítems existentes.")

        #search for nonexistent product

        search_input = self.driver.find_element(By.ID, "search")
        search_input.clear()
        search_input.send_keys("Televisor")  
        search_button = self.driver.find_element(By.CSS_SELECTOR, ".action.search")
        search_button.click()

        empty_message = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.message.notice")))
        message_text = empty_message.find_element(By.XPATH, "./div").text
        expected_message = "Your search returned no results."
        self.assertEqual(message_text, expected_message, f"El mensaje esperado '{expected_message}' no coincide con el mensaje real '{message_text}'.")



        
    @classmethod
    def tearDownClass(cls):
        # Cerrar el navegador al finalizar todas las pruebas
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
