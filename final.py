
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydub.generators import Sine
from pydub import AudioSegment
from PIL import Image

def load_image(image_path):
    """Load the image and extract RGB pixel data."""
    image = Image.open(image_path)
    
    # Resize the image to 256x256
    image = image.resize((256, 256))
    
    # Get the pixel values
    pixel_values = list(image.getdata())
    
    # Convert to a numpy array (reshape if needed)
    np_format = np.array(pixel_values).reshape((256, 256, 3))
    
    # Convert to a DataFrame (optional for RGB values)
    df = pd.DataFrame(pixel_values, columns=['Red', 'Green', 'Blue'])
    
    return image, df

def brightness_based_sonification(df, chunk_size=256):
    """Sonify image based on brightness."""
    combined_sound = None
    num_rows = len(df)
    for start_idx in range(0, num_rows, chunk_size):
        chunk = df.iloc[start_idx:start_idx + chunk_size]
        avg_rgb = chunk.mean()
        brightness = avg_rgb.mean()
        pitch = 200 + (brightness / 255) * (2000 - 200)
        volume = -20 + (brightness / 255) * 20
        tone = Sine(pitch).to_audio_segment(duration=80)
        tone = tone + volume  # Modify this line for correct volume handling
        
        combined_sound = tone if combined_sound is None else combined_sound + tone
        
    print("Sonification process finished.")
    return combined_sound

def color_based_sonification(df, chunk_size=256):
    """Sonify image by mapping RGB channels to distinct sound effects."""
    combined_sound = None
    num_rows = len(df)
    for start_idx in range(0, num_rows, chunk_size):
        chunk = df.iloc[start_idx:start_idx + chunk_size]
        avg_rgb = chunk.mean()
        red_pitch, green_pitch, blue_pitch = 300, 500, 700
        red_tone = Sine(red_pitch).to_audio_segment(duration=80) + (avg_rgb['Red'] / 255 * 20 - 20)
        green_tone = Sine(green_pitch).to_audio_segment(duration=80) + (avg_rgb['Green'] / 255 * 20 - 20)
        blue_tone = Sine(blue_pitch).to_audio_segment(duration=80) + (avg_rgb['Blue'] / 255 * 20 - 20)
        combined_tone = red_tone.overlay(green_tone).overlay(blue_tone)
        combined_sound = combined_tone if combined_sound is None else combined_sound + combined_tone
        
    print("Sonification process finished.")
    return combined_sound

def save_sound(sound, filename="output.wav"):
    """Save the generated sound to a file."""
    sound.export(filename, format="wav")
    print(f"Sound saved to {filename}")

# Modify the 'main' function to prompt for a local image path
def main():
    print("Welcome to the Image Sonification Tool!")
    
    # Prompt for the image file path
    image_path = input("Please enter the path to your image file: ")
    print(f"Image uploaded: {image_path}")
    
    try:
        image, df = load_image(image_path)
        print(f"Size of the image (RGB values): {df.shape}")  # Print the size of the dataframe
        
        print("1: Brightness-based Pitch Modulation")
        print("2: Color-based Sound Effects")
        mode = input("Select the sonification mode (1 or 2): ")
        
        if mode == "1":
            print("Generating sound using brightness-based pitch modulation...")
            sound = brightness_based_sonification(df)
        elif mode == "2":
            print("Generating sound using color-based sound effects...")
            sound = color_based_sonification(df)
        else:
            print("Invalid choice. Exiting.")
            return
        
        # Save the sound to a file
        filename = "combined_sound.wav"
        save_sound(sound, filename)
        
        # Download the file (in local environment, user can save the file directly)
        print(f"Sound file saved as {filename}.")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
