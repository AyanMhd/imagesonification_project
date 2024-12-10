# Image-to-Sound Mapping Project

## Objective
The goal of this project is to experiment with mapping pixel data (RGB values) from an image to sound properties such as pitch, volume, and duration. The pixel data is read from a CSV file containing RGB values for each pixel in the image. The program processes the data in chunks and generates a tone for each chunk based on its average RGB values. The final output is a single sound file representing the image.

## How the Mapping Works

1. **Pixel Data Processing:**
   - The program reads RGB pixel values from a CSV file. Each pixel corresponds to three columns: `R`, `G`, and `B` representing the red, green, and blue components of the pixel.
   
2. **Chunking Data:**
   - The data is processed in chunks of 256 rows at a time. Each chunk represents a small portion of the image.
   
3. **Average RGB Calculation:**
   - For each chunk of pixels, the average RGB values are calculated.
   
4. **Mapping to Sound Properties:**
   - **Pitch:** The average brightness (the mean of R, G, and B) is mapped to a pitch frequency. Brighter pixels result in higher pitch frequencies, while darker pixels result in lower frequencies.
   - **Volume:** The brightness is also mapped to the volume (in decibels). Brighter pixels have higher volume, and darker pixels have lower volume.
   - **Duration:** Each tone generated has a fixed duration of 500 milliseconds.

5. **Tone Generation:**
   - A sine wave is generated for each chunk of pixels based on its average RGB value. The resulting tones are concatenated to form a single audio file.

6. **Output:**
   - A single `.wav` file is generated, where each tone represents a 256-row chunk of the image.

## Instructions for Running the Code

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/repository-name.git
   cd repository-name

## Install dependencies: 
Make sure you have pandas and pydub installed. If not, you can install them using pip. 

## Prepare your CSV file:

The CSV file should contain three columns: Red, Green, and Blue for the RGB values of each pixel.
Example CSV structure:
css

Red, Green, Blue
120, 200,   150
255, 255,   255
0,   0,     0 

## Run the code:

Place your data.csv file in the same directory as the Python script, or update the csv_file_path variable in the script to the correct path of the CSV file.
Run the Python script:
bash
Copy code
python sound_mapping.py 

## Download the generated sound file: After running the script, a .wav file will be generated (e.g., combined_sound.wav). If running in Google Colab, you can use the following code to download the file:

from google.colab import files
files.download('combined_sound.wav') 

## Bugs and Issues
If you encounter issues such as missing columns in the CSV file (e.g., R, G, B), make sure the CSV file contains the correct headers.
The volume levels might need fine-tuning depending on the pixel brightness range.
Issue #1: (Example) - Incorrect tone generation when CSV has more than 256 rows.
Issue #2: (Example) - Pydub errors when handling large audio files; this could be resolved by increasing available memory or breaking down the chunks into smaller sizes.


