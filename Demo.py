from twilio.rest import Client
import twilio_account
import time
import subprocess
import cv2

def send_to_mobile():
	client = Client(twilio_account.sid,twilio_account.auth_token)

	message = client.messages.create(
		to = twilio_account.my_phone_number,
		from_ = twilio_account.twilio_phone_number,
		body = "Someone detected")

	print(message.sid)

def take_image():
	subprocess.run(["libcamera-still","-t", "0", "--immediate","-o", "output.jpg"])

def face_detection():
	cascPath = "/home/pi/IoT_Security_Project/haarcascade_frontalface_default.xml"
	faceCascade = cv2.CascadeClassifier(cascPath)
	image = cv2.imread("/home/pi/IoT_Security_Project/output.jpg")
	gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30,30),
		flags=cv2.CASCADE_SCALE_IMAGE
		)

	if len(faces) > 0:
		print("Face detected")
		send_to_mobile()

def main():
	while(True): 
		print("Monitoring System initiated")
		take_image()
		face_detection()
		print("Resting for 5 seconds")
		time.sleep(5)
main()
