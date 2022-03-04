#This script will perform system calls to run libcamera functions from Python.
#This script will take a picture, name it output.jpg and store it in this
#directory and finally wait 10 seconds until it repeats

import subprocess
import time

def main():
	t = 0
	while t < 10:
		subprocess.run(["libcamera-still","-t", "0", "--immediate","-o", "output.jpg"])
		print("Image taken waiting 10 seconds before the next")
		time.sleep(10)
		t+=1
main()
