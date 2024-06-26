import random
import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class Register(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_register(self):
        registerButton = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/form/div[3]/div[2]/a")
        registerButton.click()
        firstName = self.driver.find_element(By.NAME, "first_name")
        firstName.send_keys("Morgan")

        lastName = self.driver.find_element(By.NAME, "last_name")
        lastName.send_keys("Le Fay")
        phone = self.driver.find_element(By.NAME, "phone")
        phone.send_keys("3144972043")

        id_type = self.driver.find_element(By.NAME, "id_type")
        id_type.send_keys("Cédula de Ciudadanía")

        number = random.randint(1000,10000)
        id_number = self.driver.find_element(By.NAME, "id_number")
        id_number.send_keys(f"{number}")

        number = random.randint(1000,10000)
        email = self.driver.find_element(By.NAME, "email")
        email.send_keys(f"testMail{number}@mail.com")

        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("password123")

        password_confirm = self.driver.find_element(By.NAME, "password_confirm")
        password_confirm.send_keys("password123")

        sendButton = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/form/div[9]/div[1]/button")
        sendButton.click()

        text_expected = self.driver.find_element(By.NAME, 'welcome')
        self.assertEqual(text_expected.text, "Bienvenido")


class Register2(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_register(self):
        registerButton = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/form/div[3]/div[2]/a")
        registerButton.click()
        firstName = self.driver.find_element(By.NAME, "first_name")
        firstName.send_keys("Test")

        lastName = self.driver.find_element(By.NAME, "last_name")
        lastName.send_keys("User148")
        phone = self.driver.find_element(By.NAME, "phone")
        phone.send_keys("3148219093")

        id_type = self.driver.find_element(By.NAME, "id_type")
        id_type.send_keys("Cédula de Ciudadanía")

        number = random.randint(1000,10000)
        id_number = self.driver.find_element(By.NAME, "id_number")
        id_number.send_keys(f"{number}")

        number = random.randint(1000,10000)
        email = self.driver.find_element(By.NAME, "email")
        email.send_keys(f"testMail{number}@mail.com")

        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("test123")

        password_confirm = self.driver.find_element(By.NAME, "password_confirm")
        password_confirm.send_keys("test123")

        sendButton = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/form/div[9]/div[1]/button")
        sendButton.click()

        text_expected = self.driver.find_element(By.NAME, 'welcome')
        self.assertEqual(text_expected.text, "Bienvenido")

class Register3(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_register(self):
        registerButton = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/form/div[3]/div[2]/a")
        registerButton.click()
        firstName = self.driver.find_element(By.NAME, "first_name")
        firstName.send_keys("Alberto")

        lastName = self.driver.find_element(By.NAME, "last_name")
        lastName.send_keys("Salazar")
        phone = self.driver.find_element(By.NAME, "phone")
        phone.send_keys("3137875319")

        id_type = self.driver.find_element(By.NAME, "id_type")
        id_type.send_keys("Cédula de Ciudadanía")

        number = random.randint(1000,10000)
        id_number = self.driver.find_element(By.NAME, "id_number")
        id_number.send_keys(f"{number}")

        number = random.randint(1000,10000)
        email = self.driver.find_element(By.NAME, "email")
        email.send_keys(f"testMail{number}@mail.com")

        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("test123")

        password_confirm = self.driver.find_element(By.NAME, "password_confirm")
        password_confirm.send_keys("test123")

        sendButton = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/form/div[9]/div[1]/button")
        sendButton.click()

        text_expected = self.driver.find_element(By.NAME, 'welcome')
        self.assertEqual(text_expected.text, "Bienvenido")
if __name__ == "_main_":
    unittest.main()