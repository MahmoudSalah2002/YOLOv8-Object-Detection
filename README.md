# YOLOv8-Object-Detection

## Overview
This project demonstrates object detection using YOLOv8, Python, and computer vision techniques.

## Technologies
- Python
- YOLOv8
- OpenCV
- Computer Vision

## Features
- Detect objects in images.
- Display predicted classes and confidence scores.
- Support experimentation with custom-trained models.

## Project Status
Project documentation and code are being organized.

## Training Results

The model was trained to detect cats and dogs using YOLOv8.

Training evaluation plots and confusion matrices are available in the [results](results/) directory.ory.

### Results Preview

#### Training Metrics
![Training Results](results/results.png)

#### Confusion Matrix
![Confusion Matrix](results/confusion_matrix.png)

#### Normalized Confusion Matrix
![Normalized Confusion Matrix](results/confusion_matrix_normalized.png)

#### Precision-Recall Curve
![Precision-Recall Curve](results/BoxPR_curve.png)

## Author
Mahmoud Elbalat

## Installation

Clone the repository:

```bash
git clone https://github.com/MahmoudSalah2002/YOLOv8-Object-Detection.git
cd YOLOv8-Object-Detection
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To run object detection, use the trained YOLOv8 model with an image:

```bash
yolo detect predict model=weights/best.pt source=path/to/image.jpg
```

Replace `path/to/best.pt` with the location of your trained model weights, and `path/to/image.jpg` with the image you want to test.

## Supported Classes

- Cat
- Dog
