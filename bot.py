import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Inicializar WebDriver
driver_path = 'chromedriver.exe'  # Asegúrate de especificar la ruta correcta a tu WebDriver
driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)

try:
    driver.get('https://www.viajesexito.com')
    driver.maximize_window()
    #wait = WebDriverWait(driver, 10)
    time.sleep(7)
    #click=driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]')
    #click.click() #/html/body/div/div/div/div[1]   /html/body/div[6]/div/div
    element = driver.find_element(By.XPATH,'/html/body/div[6]/div/div')
    driver.execute_script("""
    var element = arguments[0];
    element.parentNode.removeChild(element);
    """, element)
    time.sleep(0.5)
    paquete = driver.find_element(By.XPATH,'/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[1]/ul/li[3]')
    time.sleep(0.5)
    print(paquete.text)
    paquete.click()
    time.sleep(0.5)
    origen = driver.find_element(By.XPATH,'/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div/input')
    time.sleep(0.5)
    origen.click()
    time.sleep(0.5)
    texto1 = driver.find_element(By.XPATH,'/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input')
    texto1.send_keys('eldorado')
    texto1.send_keys(Keys.ENTER)
    time.sleep(0.5)

    destino = driver.find_element(By.XPATH,'/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[3]/div/div/input')
    #/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[3]/div/div/input
    time.sleep(0.5)
    destino.click()
    time.sleep(0.5)
    texto2 = driver.find_element(By.XPATH,'/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input')
    texto2.send_keys('Punta Cana')
    texto2.send_keys(Keys.ENTER)
    time.sleep(0.5)
    fecha = driver.find_element(By.XPATH,'/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div/input')
    fecha.click()
    time.sleep(1)
    calendario = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div/input')))
    time.sleep(1)

    salida = driver.find_element(By.XPATH,'/html/body/div[9]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[5]/div[4]/div[2]/div[1]')
    salida.click()                        #/html/body/div[9]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[4]/div[2]/div[1]
    time.sleep(1)

    llegada = driver.find_element(By.XPATH,'/html/body/div[9]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[6]/div[4]/div[2]/div[1]')
    llegada.click()                        #/html/body/div[9]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[4]/div[2]/div[1]
    
    time.sleep(3)

    driver.execute_script("""
        var e = new KeyboardEvent('keydown', {bubbles: true, cancelable: true, keyCode: 9});  // 9 es el código de la tecla Tab
        document.dispatchEvent(e);
    """)

    driver.execute_script("""
        var e = new KeyboardEvent('keydown', {bubbles: true, cancelable: true, keyCode: 13});  // 13 es el código de la tecla Enter
        document.dispatchEvent(e);
    """)       
    time.sleep(1)
    habitaciones = driver.find_element(By.XPATH,'/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[3]/div/div/div/div')
    habitaciones.click()
    time.sleep(1)
    adicional = driver.find_element(By.XPATH,'/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[1]/button[1]')
    adicional.click()
    time.sleep(1)
    boton2 = driver.find_element(By.XPATH,'/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[2]/button')
    boton2.click()
    time.sleep(1)
    buscar = driver.find_element(By.XPATH,'/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[4]')
    buscar.click()
    time.sleep(20)
    window_handles = driver.window_handles

    driver.switch_to.window(window_handles[-1])
    
    prin=driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[4]/div/div[1]/div/span')
    print(prin.text)
    time.sleep(1)
    for i in range(10):
        precio = driver.find_element(By.XPATH,f'/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[{i+1}]/div/div/div[2]/div/div[1]/div/p[1]/span[2]')
        print(precio.text)
    time.sleep(3)

    avanzadas = driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[6]/a')
    avanzadas.click()
    time.sleep(2)
    #/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[6]/a

    aerolinea = driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[7]/div[2]/input')
    aerolinea.send_keys('avianca')
    aerolinea.send_keys(Keys.ENTER)
    #/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[7]/div[2]/input
    
    buscar = driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[8]/input')
    buscar.click()
    #/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[8]/input
    time.sleep(10)
    page_source = driver.page_source
    with open('informacion_pagina.txt', 'w', encoding='utf-8') as file:
        file.write(page_source)

    driver.save_screenshot('captura_pantalla.png')
finally:
    driver.quit()
