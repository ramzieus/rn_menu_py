from tkinter import *
import os
window = Tk()
window.resizable(0,0)
def menu():
    os.system("adb shell input keyevent 82")
def reload_app():
    os.system('adb shell input text "rr"')
def init_reactron():
    os.system("adb reverse tcp:9090 tcp:9090")

window.title("React-native menu & reload")
menu_btn = Button(window, text="Menu", command=menu)
menu_btn.grid(column=0, row=0)

reload_app_btn = Button(window, text="Reload App", command=reload_app)
reload_app_btn.grid(column=1, row=0)

init_reactron_btn = Button(window, text="Init Reactron", command=init_reactron)
init_reactron_btn.grid(column=2, row=0)


window.mainloop()