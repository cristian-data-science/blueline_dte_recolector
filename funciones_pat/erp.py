import time
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

import sys
sys.path.append("variables")
import variables as v


class funciones_globales():
    
    def __init__(self, driver):
        self.driver = driver

    def login_test(self, url, user_micro, password, tiempo):
        self.driver.get(url)
        driver = self.driver

        print("### Iniciando sesión en Dynamics 365 ###")
        sleep(1)
        print("### Ingresando usuario ###")
        email_address = driver.find_element(By.NAME, value='loginfmt')
        sleep(2)
        email_address.send_keys(user_micro)
        submit_button = driver.find_element(By.ID, value='idSIButton9')
        sleep(2)
        submit_button.click()
        print("### Ingresando password ###")
        sleep(2)
        password_d365 = driver.find_element(By.NAME, value="passwd")
        sleep(1)
        password_d365.send_keys(password)
        sleep(2)
        submit = driver.find_element(By.XPATH, value='/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div/input')
        submit.click()
        sleep(2)
        yess_button = driver.find_element(By.XPATH, value='/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input')
        yess_button.click()
        sleep(3)
        print("sesión iniciada")


        sleep(3)


    def link_recolect(self,):
        #self.driver.get(url)
        driver = self.driver
        fav = driver.find_element(By.XPATH, value= '/html/body/div[2]/div/div[5]/div/div/div[2]/div[2]')
        fav.click()
        sleep(2)
        diario_f = driver.find_element_by_link_text("Diario de facturas")
        diario_f.click()
        sleep(50)
        filtro_talonario = driver.find_element(By.XPATH, value= '/html/body/div[2]/div/div[6]/div/form[2]/div[4]/div/div[8]/div[3]/div[1]/div[4]/div/div[2]/div/div/div/div[1]/div[4]/div/div[1]/div[2]/div/div[2]/div[3]/div/div/div/div')
        filtro_talonario.click()
        sleep(2)
        text = driver.find_element(By.XPATH, value= '/html/body/div[21]/div[3]/div/div[3]/div/div/input')
        text.send_keys('ECOM-39')
        sleep(1)
        aplicar_f = driver.find_element(By.XPATH, value= '/html/body/div[21]/div[4]/button[1]')
        aplicar_f.click()
        sleep(10)
