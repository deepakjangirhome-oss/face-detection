# Face Detection using Python

A real-time face detection application built with Python and OpenCV. The program uses a Haar Cascade classifier to detect faces through a webcam and displays a rectangle around each detected face.

## Features

* Real-time face detection using a webcam
* Detects multiple faces
* Displays a rectangle around detected faces
* Shows the number of detected faces in the terminal
* Updates the face count only when the number of detected faces changes
* Converts frames to grayscale for faster face detection
* Uses histogram equalization to improve detection in different lighting conditions
* Checks whether the Haar Cascade model loads successfully
* Checks whether the camera opens successfully
* Press `Q` to close the application safely

## Technologies Used

* Python
* OpenCV
* Haar Cascade Classifier

## Project Structure

```text
face-detection/
│
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

Run the following command:

```bash
python main.py
```

The webcam will open and the application will start detecting faces.

Press `Q` to close the application.

## Requirements

* Python 3.x
* Webcam
* OpenCV

## How It Works

1. The program loads the Haar Cascade face detection model.
2. The webcam captures video frames continuously.
3. Each frame is converted to grayscale.
4. Histogram equalization improves the contrast of the image.
5. The Haar Cascade classifier detects faces in the frame.
6. A rectangle is drawn around every detected face.
7. The number of detected faces is displayed in the terminal when it changes.

## Author

Purushottam Jangir

## License

This project is created for learning and educational purposes.
