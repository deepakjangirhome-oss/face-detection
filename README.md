# Face Detection using Python

A real-time face detection application built with Python and OpenCV. The program uses a Haar Cascade classifier to detect faces through a webcam and displays useful real-time information on the video screen.

## Features

* Real-time face detection using a webcam
* Detects multiple faces
* Displays a rectangle around each detected face
* Real-time face counter displayed on the webcam screen
* FPS (Frames Per Second) counter
* Screenshot capture using the `S` key
* Automatically creates a `screenshots` folder
* Uses timestamps to create unique screenshot filenames
* Displays keyboard instructions on the webcam screen
* Shows the number of detected faces in the terminal when the count changes
* Converts frames to grayscale for face detection
* Uses histogram equalization to improve contrast in different lighting conditions
* Checks whether the Haar Cascade model loads successfully
* Checks whether the camera opens successfully
* Press `Q` to close the application safely

### Code Structure

The project is organized using separate Python functions for different responsibilities:

* `load_face_detector()` — loads and validates the Haar Cascade model
* `initialize_camera()` — initializes and validates the webcam
* `detect_faces()` — processes frames and detects faces
* `draw_information()` — displays face count, FPS, rectangles, and controls
* `save_screenshot()` — saves screenshots with timestamp-based filenames
* `main()` — controls the main application workflow

This modular structure makes the code easier to understand, maintain, and extend.


## Technologies Used

* Python
* OpenCV
* Haar Cascade Classifier

## Project Structure

```text
face-detection/
│
├── screenshots/          # Created automatically when screenshots are saved
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/deepakjangirhome-oss/face-detection.git
```

### 2. Open the project folder

```bash
cd face-detection
```

### 3. Install the required library

```bash
pip install -r requirements.txt
```

## How to Run

Run:

```bash
python main.py
```

The webcam will open and the application will start detecting faces.

## Controls

| Key | Action               |
| --- | -------------------- |
| `S` | Save a screenshot    |
| `Q` | Quit the application |

Screenshots are automatically saved in the `screenshots` folder with a timestamp-based filename.

Example:

```text
screenshot_20260911_203500.jpg
```

## Requirements

* Python 3.x
* Webcam
* OpenCV

## How It Works

1. The program loads the Haar Cascade face detection model.
2. The webcam captures video frames continuously.
3. The program calculates the current FPS.
4. Each frame is converted to grayscale.
5. Histogram equalization improves the image contrast.
6. The Haar Cascade classifier detects faces in the frame.
7. A rectangle is drawn around every detected face.
8. The number of detected faces and FPS are displayed on the webcam screen.
9. Pressing `S` saves the current frame as a screenshot.
10. Pressing `Q` closes the application safely.

## Author

Your Name

Purushottam Jangir

This project is created for learning and educational purposes.
