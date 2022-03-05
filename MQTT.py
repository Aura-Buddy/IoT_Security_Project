import paho.mqtt.client as paho
import message

def on_publish():
	print("data published")
	pass

def main():
	#connecting to arduino broker
	broker="192.168.1.184"
	port=1883

	#creating client object
	client = paho.Client("control1")

	#connect to broker
	client.connect(broker,port)
	#publish to topic and message
	ret= client.publish("IoTSecurity",message.payload)
