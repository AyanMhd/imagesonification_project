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

## 🔊 Part 2: Sound Mapping from Pixel Data  
Building on the extracted data, this assignment involved mapping pixel values to *sound properties*. 🎶  

- 🎹 *Sound Parameter Mapping*:  
   - A Python function was designed to convert pixel brightness or RGB values into sound parameters like *pitch, **volume, and **duration*.  
   - Short sound clips were generated using libraries such as *pydub* or *pygame*.  

- 🎧 *Sound Testing and Refinement*:  
   - The mapping logic was tested on small sections of the image to refine the sound generation process.  

---  

Feel free to explore the code and experiment with your own images! 🚀





