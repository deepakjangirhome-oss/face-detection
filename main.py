import cv2
import sys
import os
import time
from datetime import datetime


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

# Store the time of the previous frame
previous_time = time.time()

# Create a folder for saved screenshots
screenshot_folder = "screenshots"

if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)


try:
    # Keep the camera running continuously
    while True:

        # Capture one frame from the camera
        success, frame = camera.read()

        # Check if the frame was captured successfully
        if not success:
            print("Failed to capture frame.")
            break

        # Get the current time
        current_time = time.time()

        # Calculate the time taken to process one frame
        time_difference = current_time - previous_time

        # Calculate FPS
        if time_difference > 0:
            fps = 1 / time_difference
        else:
            fps = 0

        # Update the previous time
        previous_time = current_time

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

        # Display the FPS
        cv2.putText(
            frame, 
            f"FPS: {int(fps)}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1, 
            (0, 255, 0),
            2,
            cv2.LINE_AA
        )

        # Display instructions
        cv2.putText(
            frame,
            "S: Screenshot | Q: Quit",
            (20, frame.shape[0] - 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
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


        # Check which key pressed by user
        key = cv2.waitKey(1) & 0xFF

        # Press S to save a screenshot
        if key == ord("s"):

            # Get the current date and time
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            # Create the screenshot filename
            filename = f"screenshot_{timestamp}.jpg"

            # Create the complete file path
            filepath = os.path.join(screenshot_folder, filename)

            # Save the current camera frame
            cv2.imwrite(filepath, frame)

            print(f"Screenshot Saved: {filepath}")


        # Press Q to close the application
        if key == ord("q"):
            break


finally:
    # Release the camera
    camera.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()

