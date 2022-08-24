import time
#import unittest
from time import sleep
from datetime import date, timedelta
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select



import sys
sys.path.append("variables")
import variables as v


class funciones_globales():
    
    def __init__(self, driver):
        self.driver = driver

    def login_blue(self, url, userb, passwb):
        self.driver.get(url)
        driver = self.driver

        print("### Iniciando sesión en Blueline ###")
        sleep(1)
        user = driver.find_element(By.XPATH, value= '/html/body/div/div[1]/form/input[2]')
        user.send_keys(userb) 
        #sleep(1)
        passw = driver.find_element(By.XPATH, value= '/html/body/div/div[1]/form/input[3]')
        passw.send_keys(passwb)
        subm = driver.find_element(By.XPATH, value= '/html/body/div/div[1]/form/input[4]')
        subm.click()
        sleep(1)


    def dte_emitidos(self, url):
        self.driver.get(url)
        driver = self.driver
        #dte_emitidos = driver.find_element(By.XPATH, value='//*[@id="DTE"]/tbody/tr[1]/td/table')
        #dte_emitidos.click()

        print("### Filtrando fechas ###")
        ini = date.today() - timedelta(30)
        ini = str(ini)
        fin = date.today()
        fin = str(fin)
        sleep(1)
        ini_box = driver.find_element(By.XPATH, value ='//*[@id="FCHDESDE"]')
        ini_box.click()
        ini_box.send_keys(ini)
        ini_box.send_keys(Keys.ENTER)
        

        final_box = driver.find_element(By.XPATH, value ='//*[@id="FCHHASTA"]')
        final_box.send_keys(fin)
        #final_box.click()
        sleep(1)
        select = driver.find_element(By.XPATH, value= '//*[@id="DOCUMENTO"]')
        sleep(1)
        select.send_keys('Boleta Electrónica')
        sleep(1)
        buscar = driver.find_element(By.XPATH, value= '/html/body/fieldset/form/table[3]/tbody/tr[3]/td[1]/button') 
        buscar.click()
        print("### Descargando reporte ###")
        #WebDriverWait(self.driver, 60).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        download = driver.find_element(By.XPATH, value= '/html/body/fieldset/form/table[3]/tbody/tr[3]/td[2]/a').click()
        sleep(1)


    def cargar_datos(self):
        print("### Limpiando datos y generando nuevo reporte ###")
        df = pd.read_excel("Reporte.xls")        
        df['MOTIVO SII'] = df['MOTIVO SII'].fillna("No Informado")
        df = df.fillna(0)
        df['INVOICENUMBER'] = ("39-" + df['FOLIO'].map(str))
        print(df)
        df.to_excel("nuevo_Rep.xlsx", index = False)

    
    def to_gsheet(self):


















        """val = "next"
        x=0
        pagina = 1
        while val == "next" :
            try:

                table = driver.find_elements(By.XPATH, value='//*[@id="ExportarExcel"]/tbody')
                datos = [linea.text for linea in table]
                print(f"################# página: {pagina} ######################")
                print(datos)
                
                next_button = driver.find_elements(By.XPATH, value='/html/body/div[1]/a[*]')
                next_button[x].click()
                pagina = pagina + 1
                x=1
                    #print(len(n))
                #sleep(2)
           
            except IndexError as e:
                print(e)
                print("index error controlado")
                print("No hay página siguiente")
                val = "No_next" """