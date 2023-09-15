import pyautogui
import time
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Abre la aplicación de WhatsApp Web
webbrowser.open('https://web.whatsapp.com/')

#Espera a que la aplicación se abra
time.sleep(60)

email = driver.find_element_by_name("Pablo Amor (Tú)")
email.send_keys("tu_correo_electronico")

#Envía un mensaje de WhatsApp
pyautogui.write('Hola, voy a ingresar a zoom?')
pyautogui.press('enter')

#Abre la aplicación de Zoom Web
webbrowser.open('https://zoom.us/join')

#Espera a que la aplicación se abra
time.sleep(30)

#Entra a una reunión de Zoom
pyautogui.click(100, 100)  # Haz clic en el botón "Unirse a la reunión".

#Apaga la PC
#pyautogui.press('win')
#pyautogui.press('r')
#pyautogui.write('shutdown /s /t 0')
#pyautogui.press('enter')



