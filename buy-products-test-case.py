import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MagentoDemoTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)



    def test_5_purchase_items(self):
        # Escenario: Comprar varios artículos en el sitio


        #------------------------------------- INICIO DE SESION -------------------------------------#

        self.driver.get("https://magento.softwaretestingboard.com/")
        
        #Darle click al botón de inicio de sesion dentro de la pagina principal
        sign_in_link = self.driver.find_element(By.LINK_TEXT, "Sign In")
        sign_in_link.click()

        #Llenar datos de login
        #sign_in_form = self.driver.find_elements(By.ID, "login-form")
        email_input = self.driver.find_element(By.ID, "email")
        email_input.send_keys("mariajesusvargas9@example.com")
        password_input = self.driver.find_element(By.ID, "pass")
        password_input.send_keys("Password123.123")
        self.driver.find_element(By.ID, "send2").click()



        #----------------------------- AÑADIR PRIMER PRODUCTO A CARRITO -----------------------------#

        ignore_list = [ElementNotVisibleException, ElementNotSelectableException]
        wait = WebDriverWait(self.driver, timeout=10, poll_frequency=1, ignored_exceptions=ignore_list)

        # Dirigirse a la pagina de Hoodies & Sweatshirts
        # women = id-4, tops = id-9, Hoddies & Sweatshirts = id-12
        ActionChains(self.driver)\
            .move_to_element(self.driver.find_element(By.XPATH, "//*[@id='ui-id-4']"))\
            .move_to_element(self.driver.find_element(By.XPATH, "//*[@id='ui-id-9']"))\
            .click(self.driver.find_element(By.XPATH, "//*[@id='ui-id-12']"))\
            .perform()

        # Agregar al carrito el producto Ariel Roll Sleeve Sweatshirt en talla S color verde
        self.driver.find_element(By.LINK_TEXT, "Ariel Roll Sleeve Sweatshirt").click()
        self.driver.find_element(By.XPATH, "//div[text()='S']").click()
        self.driver.find_element(By.XPATH, "//*[@id='option-label-color-93-item-53']").click()
        self.driver.find_element(By.XPATH, "//*[text()='Add to Cart']").click()

        time.sleep(2)

        # Verificar que se haya agregado el primer producto exitosamente al carrito
        product_1_added_message = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='maincontent']/div[1]/div[2]/div/div/div")))
        self.assertEqual(product_1_added_message.text, "You added Ariel Roll Sleeve Sweatshirt to your shopping cart.")



        #----------------------------- AÑADIR SEGUNDO PRODUCTO A CARRITO -----------------------------#

        # Dirigirse a landing page y clickear comprar pantalones
        self.driver.find_element(By.CLASS_NAME, "logo").click()
        self.driver.find_element(By.XPATH, "//*[text()='Shop Pants']").click()

        #Agregar al carrito el producto Ida Workout Parachute Pant en talla 28 color azul
        self.driver.find_element(By.LINK_TEXT, "Ida Workout Parachute Pant").click()
        self.driver.find_element(By.XPATH, "//div[text()='28']").click()
        self.driver.find_element(By.XPATH, "//*[@id='option-label-color-93-item-50']").click()
        self.driver.find_element(By.XPATH, "//*[text()='Add to Cart']").click()

        # Verificar que se haya agregado el segundo producto exitosamente al carrito
        product_2_added_message = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='maincontent']/div[1]/div[2]/div/div/div")))
        self.assertEqual(product_2_added_message.text, "You added Ida Workout Parachute Pant to your shopping cart.")


        #----------------------------- AÑADIR TERCER PRODUCTO A CARRITO -----------------------------#

        # Dirigirse a la pagina de Tops
        # Tops = id-17
        ActionChains(self.driver)\
            .move_to_element(self.driver.find_element(By.XPATH, "//*[text()='Men']"))\
            .click(self.driver.find_element(By.XPATH, "//*[@id='ui-id-17']"))\
            .perform()

        #Filtrar por precio $30.00 - $39.99 y color verde
        self.driver.find_element(By.XPATH, "//*[text()='Price']").click()
        self.driver.find_element(By.XPATH, "//*[text()='$30.00']").click()
        self.driver.find_element(By.XPATH, "//div[text()='Color']").click()
        self.driver.find_element(By.XPATH, "//div[@class='swatch-option color ' and @option-label='Green']").click()

        #Agregar al carrito Deion Long-Sleeve EverCool™ Tee talla M
        self.driver.find_element(By.XPATH, "//div[text()='M']").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()= 'Add to Cart']")))
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[text()= 'Add to Cart']").click()

        # Verificar que se haya agregado el tercer producto exitosamente al carrito
        product_3_added_message = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='maincontent']/div[2]/div[2]/div/div/div")))
        #product_3_added_message = self.driver.find_element(By.XPATH, "//*[@id='maincontent']/div[2]/div[2]/div/div/div")
        self.assertEqual(product_3_added_message.text, "You added Deion Long-Sleeve EverCool™ Tee to your shopping cart.")



        #----------------------------- COMPRAR LO QUE HAY EN EL CARRITO -----------------------------#

        #Ver el carrito
        self.driver.find_element(By.XPATH, "//a[@class='action showcart']").click()
        self.driver.find_element(By.ID, "top-cart-btn-checkout").click()

        #Llenar datos de shipping y hacer la compra si no existen
        try:
            self.driver.find_element(By.XPATH, "//div[@class='shipping-address-item selected-item']")
        except NameError:
            self.driver.find_element(By.NAME, "street[0]").send_keys("13th Street. 47 W 13th St")   #Address
            self.driver.find_element(By.NAME, "city").send_keys("New York")                         #City
            self.driver.find_element(By.NAME, "region_id").click()                                  #Open dropdown State selector
            self.driver.find_element(By.XPATH, "//option[text()='New York']").click()               #Select State
            self.driver.find_element(By.NAME, "postcode").send_keys("10011")                        #Zip Code
            self.driver.find_element(By.NAME, "telephone").send_keys("+1 123456789")                #Phone Number

        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Best Way']")))
        self.driver.find_element(By.XPATH, "//*[text()='Best Way']").click()                    #Shipping Method
        self.driver.find_element(By.XPATH, "//*[text()='Next']").click()                        #Next Step Button
        time.sleep(3)
        #wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Place Order']")))
        self.driver.find_element(By.XPATH, "//button[@title='Place Order']").click()                 #Place Order

        #Verificar compra
        #time.sleep(2)
        wait.until(EC.url_changes("https://magento.softwaretestingboard.com/checkout/#payment"))
        self.assertEqual(self.driver.current_url, "https://magento.softwaretestingboard.com/checkout/onepage/success/")



       #--------------------------------------- CERRAR SESION ---------------------------------------#

        self.driver.get("https://magento.softwaretestingboard.com/customer/account/logout/%22")

        # Verificar que se haya cerrado sesión correctamente
        self.assertIsNotNone(self.driver.find_element(By.LINK_TEXT, "Sign In"))



    @classmethod
    def tearDownClass(cls):
        # Cerrar el navegador al finalizar todas las pruebas
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()