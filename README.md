# Slouch Detection Application

## Overview
This project aims to create an application that raises alerts when it detects user slouching. The application utilizes the YOLOv8 model for real-time keypoint detection and can be adapted for various pose detection applications based on the dataset used.

## Requirements

- Python 3.11
- Jupyter Notebook or VSCode with Jupyter extension
- [Ultralytics YOLOv8](https://github.com/ultralytics/yolov8)

## Usage

### Step 1: Train the Model
Before running the live prediction script, you need to train the model using `posdet.ipynb`. This notebook contains the necessary code for model training and inferencing. Ensure that you have chosen appropriate training images as the model is sensitive to input data. 

### Step 2: Run the Live Prediction
Once the model is trained, you can run `livepred.py` to start detecting keypoints in real-time. This script utilizes the trained model to analyze the user's posture by accessing the camera on the device.

```bash
python livepred.py
```

## Important Notes

- The current model is configured for two classes but can be extended to include more. Adapt the training dataset accordingly.
- Body position normalization is yet to be implemented, which is crucial for improving detection accuracy.
- The choice of training images is critical; ensure they represent a variety of body positions and conditions for effective training.

## Acknowledgments
- [YOLOv8](https://github.com/ultralytics/yolov8) by Ultralytics for the pose detection model.

---
