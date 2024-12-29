# 🌌 Image Sonification and Data Extraction Project

This project delves into the fascinating process of *image sonification* and *data extraction*, encompassing two key assignments. 🎯 
  


## How to use this tool?
# Image Sonification Tool

This tool allows users to sonify an image by converting its pixel values (RGB) into sound. The sonification can be based on either brightness-based pitch modulation or color-based sound effects.

## Features

- Upload an image and generate sound based on the image’s pixel values.
- Choose between two sonification modes:
  - **Brightness-based Pitch Modulation**: The brightness of the image influences the pitch and volume of the sound.
  - **Color-based Sound Effects**: Each RGB channel is mapped to a distinct sound.

## Setup Instructions

To run this tool on your local machine or in a cloud environment like Google Colab, follow these steps:

### Prerequisites

1. **Python 3.x** installed on your system.
2. **Install dependencies**: Create a virtual environment and install the required packages by running:

   ```bash
   pip install -r requirements.txt
   
## Running the Tool  

 1. Clone the repository to your local machine:  

  git clone https://github.com/your-username/image-sonification.git  
  
  Next change the directory to the main directory 
  
      cd image-sonification 

 2. Run the script: 

python final.py 

 3. When prompted, upload an image and select one of the two sonification modes.

 4. The sound file will be generated and saved in the local directory. 

## Dependencies : 

   pydub
   Pillow
   numpy
   pandas 

## You can install all dependencies with: 

   pip install -r requirements.txt  

## Release Version
    The current version of the tool is v1.0. 

You can upload your own images to generate sound, but a sample image (initial_image.png) and its corresponding sonified 
sound file (outputdata/generatedsoundfrompixelvalues) are included in the repository.




