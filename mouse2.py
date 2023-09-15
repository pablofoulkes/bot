import pyautogui
import webbrowser
import schedule
import time
import os

def apagar_pc():
    time.sleep(10)
    os.system("shutdown /s /t 0")


# Esta función envía un mensaje de WhatsApp con el texto especificado.
def enviarWhatsapp(texto):
    webbrowser.open('https://web.whatsapp.com/send?phone=+5493624815669')
    time.sleep(30)
    pyautogui.typewrite(texto)
    pyautogui.press('enter')
    time.sleep(20)

def unirseAReunionZoom():
    webbrowser.open('https://utn.zoom.us/wc/85386596127/join?_x_zm_rtaid=m_wRFbPfS-6oKr65IJ-f0Q.1694743823515.8303e7fbae155de0010dfbec10d6ae6a&_x_zm_rhtaid=669')
    time.sleep(10)
    time.sleep(5)
    pyautogui.click(x= 865, y=539)
    time.sleep(5)
    pyautogui.click(x= 865, y=539)
    time.sleep(5)
    pyautogui.click(x= 865, y=539)
    # Esperar unos segundos para que Zoom se abra
    #pyautogui.typewrite('DFC-UTN')  # Escribir el código de acceso
    #pyautogui.press('enter')  # Presionar Enter para unirse

# Programar el envío de mensajes de WhatsApp a horas específicas.
schedule.every().day.at("17:55").do(enviarWhatsapp, "entrando a zoom")
schedule.every().day.at("17:58").do(unirseAReunionZoom)  

schedule.every().day.at("20:08").do(enviarWhatsapp, "apagando")
schedule.every().day.at("21:07").do(enviarWhatsapp, "no apago")

# Este bucle mantiene el programa en ejecución y verifica las tareas programadas.
while True:
    schedule.run_pending()
    time.sleep(1)
