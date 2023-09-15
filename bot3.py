
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Configuración del navegador
driver = webdriver.Chrome()
driver.get("https://zoom.us/signin")

# Ingresa el correo electrónico y la contraseña
email = driver.find_element_by_name("email")
email.send_keys("tu_correo_electronico")

password = driver.find_element_by_name("password")
password.send_keys("tu_contraseña")

# Inicia sesión
login_button = driver.find_element_by_css_selector(".btn.btn-primary.btn-block")
login_button.click()

# Espera a que se cargue la página
time.sleep(5)

# Ingresa el ID de la reunión
meeting_id = driver.find_element_by_name("meetingId")
meeting_id.send_keys("el_id_de_la_reunion")

# Inicia la reunión
join_button = driver.find_element_by_css_selector(".btn.btn-primary.btn-block")
join_button.click()

# Espera a que se cargue la página
time.sleep(5)

# Acepta los permisos de acceso a la cámara y el micrófono
pyautogui.press("enter")
pyautogui.press("enter")

# Espera a que termine la reunión
time.sleep(60)

# Cierra el navegador
driver.quit()