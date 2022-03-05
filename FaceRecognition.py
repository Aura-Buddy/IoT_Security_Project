import face_recognition

def main():
	image = face_recognition.load_image_file("/home/pi/IoT_Security_Project/output.jpg")

	#This encodes the image
	face_encoding = face_recognition.face_encodings(image)
	print("This is face encoding", face_encoding) #For testing, delete after

	unknown_picture = face_recognition.load_image_file("/home/pi/IoT_Security_Project/compare.jpg")
	unknown_face_encoding = face_recognition.face_encodings(unknown_picture)
	print("This is face encoding of unknown picture", unknown_face_encoding) #For testing, delete after

	results = face_recognition.compare_faces(face_encoding, unknown_face_encoding)
	print("This is the result", results)

	if results:
		print("These faces match")
	else:
		print("These faces do not match")

main()
