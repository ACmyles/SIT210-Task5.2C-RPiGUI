import RPi.GPIO as GPIO
import time
import tkinter

gui = tkinter.Tk()
gui.title("RPiGUI LED Control")

state = tkinter.IntVar()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

GPIO.output(19, GPIO.LOW)
GPIO.output(21, GPIO.LOW)
GPIO.output(23, GPIO.LOW)


def toggle(led):
    if (led == 19):
        GPIO.output(led, GPIO.HIGH)
        GPIO.output(21, GPIO.LOW)
        GPIO.output(23, GPIO.LOW)
    elif (led == 21):
        GPIO.output(led, GPIO.HIGH)
        GPIO.output(19, GPIO.LOW)
        GPIO.output(23, GPIO.LOW)
    elif (led == 23):
        GPIO.output(led, GPIO.HIGH)
        GPIO.output(19, GPIO.LOW)
        GPIO.output(21, GPIO.LOW)


gui_red_button = tkinter.Radiobutton(
    gui, text="Red", variable=state, value=23, command=lambda: toggle(23), width=15)
gui_green_button = tkinter.Radiobutton(
    gui, text="Green", variable=state, value=19, command=lambda: toggle(19), width=15)
gui_blue_button = tkinter.Radiobutton(
    gui, text="Blue", variable=state, value=21, command=lambda: toggle(21), width=15)
exit_button = tkinter.Button(gui, text="Exit", command=gui.destroy, width=15)

gui_red_button.pack()
gui_green_button.pack()
gui_blue_button.pack()
exit_button.pack()

gui.mainloop()
GPIO.cleanup()
