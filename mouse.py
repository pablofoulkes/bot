import pyautogui
import webbrowser
import schedule
import time
import os
print("/t", pyautogui.displayMousePosition())
pyautogui.click(1,1)

#para apagar la pc
#pyautogui.click(x= 28, y=751)
#pyautogui.sleep(10)
#pyautogui.click(x= 25, y=702)
#pyautogui.sleep(10)
#pyautogui.click(x= 16, y=622)

#para enviar whatsapp

#from time import sleep

#webbrowser.open('https://web.whatsapp.com/send?phone=+5493624815669')
#sleep(10)
#pyautogui.typewrite("apagando la pc")
#pyautogui.press('enter')



# Esta función apaga la computadora.
def apagar_pc():
    webbrowser.open('https://web.whatsapp.com/send?phone=+5493624815669')
    time.sleep(30)
    pyautogui.typewrite("apagando la pc")

    pyautogui.press('enter')

    os.system("shutdown /s /t 0")

def enviarWhatsapp(texto):
  webbrowser.open('https://web.whatsapp.com/send?phone=+5493624815669')
  time.sleep(30)
  pyautogui.typewrite(texto)
  pyautogui.press('enter')
  time.sleep(20)
  #cierra pagina web
  #webbrowser.get().close()

# Esta línea programa la función `apagar_pc()` para que se ejecute todos los días a las 20:00.
#schedule.every().day.at("20:35").do(apagar_pc)
schedule.every().day.at("22:54").do(enviarWhatsapp("prueba 2230"))
schedule.every().day.at("22:55").do(enviarWhatsapp("prueba 2240"))
schedule.every().day.at("22:56").do(enviarWhatsapp("prueba 2250"))

# Este bucle mantiene el programa en ejecución.
while True:
  schedule.run_pending()
  print("estoy aca")
  time.sleep(1)

