import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By



class MagentoDemoTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Configuración del controlador de Chrome
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)  # Espera implícita de 10 segundos

    def test_4_compare_items(self):
        # Escenario: Crear una cuenta nueva
        self.driver.get("https://magento.softwaretestingboard.com/")


        # Realiza acciones en el sitio web para seleccionar y comparar los elementos
        self.driver.find_element(By.XPATH, "//*[@id='maincontent']/div[3]/div/div[2]/div[1]/div/a[1]/span/span[2]").click()

        
        self.driver.find_element(By.LINK_TEXT, "Portia Capri").click()
        pants1_name = self.driver.find_elements(By.XPATH, "//*[@id='maincontent']/div[2]/div/div[1]/div[1]/h1/span")[0].text
        pants1_price = self.driver.find_elements(By.ID, "product-price-1903")[0].text

        self.driver.back()  # Regresa a la página anterior

        self.driver.find_element(By.LINK_TEXT, "Sylvia Capri").click()
        pants2_name = self.driver.find_elements(By.XPATH, "//*[@id='maincontent']/div[2]/div/div[1]/div[1]/h1/span")[0].text
        pants2_price = self.driver.find_elements(By.ID, "product-price-1889")[0].text
        
        self.driver.back()
        self.driver.back()


        self.driver.find_element(By.XPATH, "//*[@id='maincontent']/div[3]/div/div[2]/div[1]/div/a[2]/span[2]/span[2]").click()

        
        self.driver.find_element(By.LINK_TEXT, "Diva Gym Tee").click()
        tee1_name = self.driver.find_elements(By.XPATH, "//*[@id='maincontent']/div[2]/div/div[1]/div[1]/h1/span")[0].text
        
        tee1_price = self.driver.find_elements(By.ID, "product-price-1540")[0].text

        self.driver.back()  # Regresa a la página anterior

        self.driver.find_element(By.LINK_TEXT, "Desiree Fitness Tee").click()
        tee2_name = self.driver.find_elements(By.XPATH, "//*[@id='maincontent']/div[2]/div/div[1]/div[1]/h1/span")[0].text
        tee2_price = self.driver.find_elements(By.ID, "product-price-1588")[0].text
        
        self.driver.back()
        self.driver.back()
        

        # Realiza la comparación utilizando assert
        assert pants1_price != pants2_price, "Los precios de los pantalones no son iguales"

        if pants1_price < pants2_price:
            print("El precio de " + pants1_name + " es menor que el precio de " + pants2_name)
        else:
            print("El precio de " + pants2_name + " es menor que el precio de " + pants1_name)



        assert tee1_price != tee2_price, "Los precios de las camisas no son iguales"

        if tee2_price < tee1_price:
            print("El precio de " + tee2_name + " es menor que el precio de " + tee1_name)
        else:
            print("El precio de " + tee1_name + " es menor que el precio de " + tee2_name)



    @classmethod
    def tearDownClass(cls):
        # Cerrar el navegador al finalizar todas las pruebas
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()