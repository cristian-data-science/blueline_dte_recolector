import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from funciones_pat.blueline import funciones_globales

from selenium.webdriver.common.action_chains import ActionChains
import os

chrome_options = Options()
chrome_options.headless = True
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')


import variables as v

class base_test(unittest.TestCase):

    def setUp(self):
        
        # Descomentar linea siguiente para ejecución en windows
        
        #self.driver = webdriver.Chrome(executable_path= r'C:\chrome_driver\chromedriver.exe',options=chrome_options)
        
         
        # Descomentar linea siguiente para ejecución en linux
        self.driver = webdriver.Chrome(options=chrome_options)
        
        # driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
        driver = self.driver

        # codigo para permitir las descargas de archivos en headless mode
        #from selenium.webdriver.common.action_chains import ActionChains
        #import os
        params = {'behavior': 'allow', 'downloadPath': os.getcwd()}
        driver.execute_cdp_cmd('Page.setDownloadBehavior', params)


        # este implicity contrala el time out 
        driver.implicitly_wait(60)
        driver.maximize_window()
        #driver.get("https://patagonia-testpos.sandbox.operations.dynamics.com/")        
    

    def test1(self):
        driver = self.driver
        f = funciones_globales(driver)
        f.login_blue(v.url_blue_line, v.user_blueline, v.pass_blueline)
        f.dte_emitidos(v.url_dte_emitidos)
        f.cargar_datos()
        f.to_gsheet()


    def tearDown(self):
        driver = self.driver
        driver.close()
        

if __name__ == '__main__':
    unittest.main()




