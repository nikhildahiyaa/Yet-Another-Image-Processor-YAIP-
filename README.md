# Yet Another Image Processor (YAIP)

## Introduction

This project is an image processing application developed as part of the CMPT 120 course at Simon Fraser University during Fall 2021. It allows users to apply various image manipulation techniques, such as filters, resizing, rotating images, and even a special feature to detect a fish in an image for a cat.

## Features

### Basic Image Manipulations
- **Red Filter:** Retains only the red channel, setting green and blue to zero.
- **Green Filter:** Retains only the green channel, setting red and blue to zero.
- **Blue Filter:** Retains only the blue channel, setting red and green to zero.
- **Sepia Filter:** Applies a sepia tone to the image.
- **Warm Filter:** Enhances the red tones in the image.
- **Cold Filter:** Enhances the blue tones in the image.

### Advanced Image Manipulations
- **Rotate Left:** Rotates the image 90 degrees counter-clockwise.
- **Rotate Right:** Rotates the image 90 degrees clockwise.
- **Double Size:** Increases the image size by a factor of 2.
- **Half Size:** Decreases the image size by a factor of 2.
- **Fish Detection:** Detects a yellow fish in the image and draws a green bounding box around it.

### System Options
- **Open Image:** Load an image from your computer.
- **Save Image:** Save the current state of the image.
- **Reload Image:** Reload the original image.
- **Quit:** Exit the application.

## Project Structure

- **`main.py`:** The main driver file that runs the application. It handles user inputs and displays the interface.
- **`cmpt120imageProjHelper.py`:** Contains helper functions for loading, saving, and displaying images.
- **`cmpt120imageManip.py`:** Contains the core image manipulation functions, such as applying filters, resizing, rotating, and fish detection.
- **`fish.jpg`:** The image of the fish used for testing the fish detection feature.
- **`project-photo.jpg`:** The image used in the project, which includes a cat for the fish detection feature.

## Prerequisites

- **Python 3.x**
- Required Python packages:
  - `pygame`
  - `numpy`
  - `tkinter` (usually included with Python)

## Installation

- **Install the required packages**:
    ```bash
    pip3 install pygame numpy
    ```

## Running the Project

To run the application, execute the `main.py` file:

```bash
python3 main.py
