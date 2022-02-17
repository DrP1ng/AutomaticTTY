from sys import argv
from time import sleep
from pynput.keyboard import Key, Controller

keyboard = Controller()
try:
	version = argv[1]
except:
	version = ""

sleep(4)
keyboard.type("python"+version+" -c 'import pty; pty.spawn(\"/bin/bash\")'")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(0.2)
keyboard.press(Key.ctrl)
keyboard.press('z')
keyboard.release(Key.ctrl)
keyboard.release('z')
sleep(0.2)
keyboard.type("stty raw -echo; fg")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(0.2)
keyboard.type("reset")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(0.2)
keyboard.type("xterm")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(0.2)
keyboard.type("export TERM=xterm")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(0.2)
keyboard.type("export SHELL=bash")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(0.2)
keyboard.press(Key.ctrl)
keyboard.press('l')
keyboard.release(Key.ctrl)
keyboard.release('l')
sleep(1)
keyboard.type("tty")
keyboard.press(Key.enter)
keyboard.release(Key.enter)

