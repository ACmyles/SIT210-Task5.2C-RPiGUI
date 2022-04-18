import RPi.GPIO as GPIO
import time
import tkinter

gui = tkinter.Tk()
gui.title("RPiGUI LED Control")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)


def toggle(led):
    if GPIO.input(led):
        GPIO.output(led,GPIO.LOW)
    else:
        GPIO.output(led,GPIO.HIGH)

gui_blue_button = tkinter.Button(gui,text="Toggle Blue LED",command=lambda: toggle(21),width=15)
gui_green_button = tkinter.Button(gui,text="Toggle Green LED",command=lambda: toggle(19),width=15)
gui_yellow_button = tkinter.Button(gui,text="Toggle Yellow LED",command=lambda: toggle(23),width=15)

gui_blue_button.pack()
gui_green_button.pack()
gui_yellow_button.pack()

gui.mainloop()