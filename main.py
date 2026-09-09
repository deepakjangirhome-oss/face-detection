import cv2
import sys


# Load Haar Cascade Face Detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Check if the face detection model loaded successfully
if face_cascade.empty():
    print("Error: Haar Cascade failed to load!")
    sys.exit()


# Open the camera
camera = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not camera.isOpened():
    print("Error: Could not open camera.")
    sys.exit()


# Store the previous number of detected faces
# -1 is used initially because the number of faces starts from 0
previous_faces = -1


try:
    # Keep the camera running continuously
    while True:

        # Capture one frame from the camera
        success, frame = camera.read()

        # Check if the frame was captured successfully
        if not success:
            print("Failed to capture frame.")
            break


        # Convert the colored frame into grayscale
        # Face detection works better and faster with grayscale images
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        # Improve the contrast of the grayscale image
        # This can help detect faces in different lighting conditions
        gray = cv2.equalizeHist(gray)


        # Detect faces in the camera frame
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(80, 80)
        )


        # Count how many faces are currently detected
        current_faces = len(faces)


        # Print only when the number of faces changes
        if current_faces != previous_faces:
            print("Faces detected:", current_faces)
            previous_faces = current_faces

        # Display the face count on the camera screen
        cv2.putText(
            frame,
            f"Faces Detected: {current_faces}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
            cv2.LINE_AA
        )


        # Go through every detected face
        for (x, y, w, h) in faces:

            # Draw a green rectangle around the detected face
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )


        # Display the camera frame in a window
        cv2.imshow("Face Detection using Python", frame)


        # Press the Q key to close the camera window
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


finally:
    # Release the camera
    camera.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()

