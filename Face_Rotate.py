# -------------------- THIS IS USED TO SHOW TO ROTATION OF THE IMAGE FOR FACE RECOGNITION SYSTEMS ----------------------
# ----------------------------------------------------------------------------------------------------------------------

import cv2                                                                                       # Importing the opencv
import NameFind
WHITE = [255, 255, 255]

fc = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml')          # import the Haar cascades for face ditection
ec = cv2.CascadeClassifier('Haar/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)                                                                                # Camera object

while True:
    r, i = cap.read()
    gray = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)                                              # Convert the Camera to gray
    faces = fc.detectMultiScale(gray, 1.3, 5)                                 # Detect the faces and store the positions
    for (x, y, w, h) in faces:                                                    # Frames  LOCATION X, Y  WIDTH, HEIGHT
        FaceImage = gray[y - int(h / 2): y + int(h * 1.5), x - int(x / 2): x + int(w * 1.5)]  # The Face is isolated and cropped
        Img = (NameFind.DetectEyes(FaceImage))
        cv2.putText(gray, "FACE DETECTED", (x+int(w/2), y-5), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)
        if Img is not None:
            frame = Img                                                                        # Show the detected faces
        else:
            frame = gray[y: y+h, x: x+w]
        cv2.imshow("CAPTURED PHOTO", frame)                                                    # show the captured image
    cv2.imshow('Face Recognition System Capture Faces', gray)                                           # Show the video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()