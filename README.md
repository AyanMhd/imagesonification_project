# 🌌 Image Sonification and Data Extraction Project

This project delves into the fascinating process of *image sonification* and *data extraction*, encompassing two key assignments. 🎯 

---

## 📸 Part 1: Image Data Extraction and Visualization  
The objective of this assignment was to explore *image sonification* by extracting pixel data from a high-resolution galaxy image 🌠. Here's how it was achieved:  

- 🛠 *Data Extraction*:  
   - Using Python libraries like *OpenCV* or *PIL*, pixel intensities or RGB values were extracted from the image.  
   - The extracted data was stored in a structured format, such as a *CSV file*.  

- 📊 *Data Visualization*:  
   - The distribution of pixel intensities was visualized using *matplotlib* to gain insights into the image data.  

This step laid the foundation for understanding the relationship between pixel data and potential sound mappings. 🎵  

---

## 🔊 Part 2: Sound Mapping from Pixel Data  
Building on the extracted data, this assignment involved mapping pixel values to *sound properties*. 🎶  

- 🎹 *Sound Parameter Mapping*:  
   - A Python function was designed to convert pixel brightness or RGB values into sound parameters like *pitch, **volume, and **duration*.  
   - Short sound clips were generated using libraries such as *pydub* or *pygame*.  

- 🎧 *Sound Testing and Refinement*:  
   - The mapping logic was tested on small sections of the image to refine the sound generation process.  

---  

Feel free to explore the code and experiment with your own images! 🚀

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
cd image-sonification 

 2. Run the script: 

python final.py 

 3. When prompted, upload an image and select one of the two sonification modes.

 4. The sound file will be generated and saved in the local directory. 

## Dependencies : 

# pydub
# Pillow
# numpy
# pandas 

## You can install all dependencies with: 

# pip install -r requirements.txt 




