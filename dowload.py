from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from tkinter import ttk
from tkinter import *
import requests

link = None

#* root.destroy ( закрытие окна после нажатие кнопки, сразу же)
def dowloading():
    global link
    link = entry.get()
    root.destroy()
    return link


root = Tk()
root.geometry("300x300")
root.title("Dowloading videos ")

label = ttk.Label(text="Ссылка на видео: ")
label.pack(anchor=SW,padx=6,pady=6)

entry = ttk.Entry(font=("Arial",10))
entry.pack(anchor=NW,padx=6,pady=6)
btn = ttk.Button(text="Скачать",command=dowloading)
btn.pack(anchor=NW,padx=6,pady=6)
root.mainloop()


if link:

    browser = webdriver.Chrome()
    browser.get("https://www.freemake.com/ru/free_video_downloader_best/?ysclid=lyptdwupbx715383319")

    inputElement = WebDriverWait(browser,15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,"input[name='link']"))
    )
    inputElement.send_keys(link)


    time.sleep(3)
    btnElement = WebDriverWait(browser,15).until(
        EC.presence_of_element_located((By.CLASS_NAME,"fwd__topblock__download__video"))
    )
    btnElement.click()
    time.sleep(10)
else:
    print("Ссылка пуста")

    