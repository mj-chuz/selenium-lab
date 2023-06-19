import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class MagentoDemoTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Configuración del controlador de Chrome
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)  # Espera implícita de 10 segundos

    def test_1_create_account(self):
        # Escenario: Crear una cuenta nueva
        self.driver.get("https://magento.softwaretestingboard.com/")


        sign_in_link = self.driver.find_element(By.LINK_TEXT, "Create an Account")
        sign_in_link.click()

        # Completar el formulario de creación de cuenta con datos de ejemplo
        create_account_form1 = self.driver.find_elements(By.ID, "form-validate")
        create_account_form = create_account_form1[0]
        first_name_input = create_account_form.find_element(By.ID, "firstname")
        first_name_input.send_keys("Maria")
        last_name_input = create_account_form.find_element(By.ID, "lastname")
        last_name_input.send_keys("Vargas")
        email_input = create_account_form.find_element(By.ID, "email_address")
        email_input.send_keys("mariajesusvargas9@example.com")
        password_input = create_account_form.find_element(By.ID, "password")
        password_input.send_keys("Password123.123")
        confirm_password_input = create_account_form.find_element(By.ID, "password-confirmation")
        confirm_password_input.send_keys("Password123.123")
        create_account_button = create_account_form.find_element(By.XPATH, "//button[@title='Create an Account']")
        create_account_button.click()

        time.sleep(2)

        # Verificar que se haya creado la cuenta exitosamente
        welcome_message = self.driver.find_element(By.XPATH, "//*[@id='maincontent']/div[1]/div[2]/div/div/div")
        self.assertEqual(welcome_message.text, "Thank you for registering with Main Website Store.")

        # Cerrar sesión
        self.driver.get("https://magento.softwaretestingboard.com/customer/account/logout/%22")

        # Verificar que se haya cerrado sesión correctamente
        sign_in_link_again = self.driver.find_element(By.LINK_TEXT, "Sign In")
        self.assertIsNotNone(sign_in_link_again)

    # def test_2_wishlist(self):
    #     # Escenario: Agregar/eliminar artículos del Wishlist
    #     self.driver.get("https://magento.softwaretestingboard.com/")
    #     # Agregar el código necesario para agregar y eliminar artículos del Wishlist
    #     # Realizar los asserts necesarios para verificar el resultado

    # def test_3_search_existing_item(self):
    #     # Escenario: Utilizar el buscador - Ítems existentes
    #     self.driver.get("https://magento.softwaretestingboard.com/")
    #     # Agregar el código necesario para realizar una búsqueda de un ítem existente
    #     # Realizar los asserts necesarios para verificar el resultado

    # def test_4_search_non_existing_item(self):
    #     # Escenario: Utilizar el buscador - Ítems no existentes
    #     self.driver.get("https://magento.softwaretestingboard.com/")
    #     # Agregar el código necesario para realizar una búsqueda de un ítem no existente
    #     # Realizar los asserts necesarios para verificar el resultado

    # def test_5_compare_items(self):
    #     # Escenario: Realizar una comparación de varios ítems en el sitio
    #     self.driver.get("https://magento.softwaretestingboard.com/")
    #     # Agregar el código necesario para seleccionar y comparar varios ítems
    #     # Realizar los asserts necesarios para verificar el resultado

    # def test_6_purchase_items(self):
    #     # Escenario: Comprar varios artículos en el sitio
    #     self.driver.get("https://magento.softwaretestingboard.com/")
    #     # Agregar el código necesario para seleccionar y comprar varios artículos
    #     # Utilizar menús, filtros y opciones en la página
    #     # Realizar los asserts necesarios para verificar el resultado

    @classmethod
    def tearDownClass(cls):
        # Cerrar el navegador al finalizar todas las pruebas
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()