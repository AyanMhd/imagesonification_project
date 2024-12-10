
!pip install pydub
from pydub.generators import Sine
import pandas as pd
import numpy as np
def generate_tone(pitch, duration, volume):
    """
    Generate a tone with a specific pitch, duration, and volume using pydub.

    Parameters:
        pitch (float): Frequency of the tone in Hz.
        duration (float): Duration of the tone in milliseconds.
        volume (float): Volume of the tone in decibels.
    """
    # Create a sine wave with the given pitch and duration
    tone = Sine(pitch).to_audio_segment(duration=duration)

    # Adjust the volume (pydub uses dB; positive increases, negative decreases)
    tone = tone + volume
    return tone

def generate_sounds_from_csv(csv_file, chunk_size=256):
    """
    Generate a single sound file by processing chunks of pixel data and mapping
    the average RGB values of each chunk to a tone.

    Parameters:
        csv_file (str): Path to the CSV file containing RGB pixel data.
        chunk_size (int): Number of rows to process at a time (default is 256).
    """
    # Read the CSV file
    data = pd.read_csv('csvformat.csv')

    # Initialize an empty audio segment to combine all the tones
    combined_sound = None

    # Process the data in chunks of specified size
    num_rows = len(data)
    for start_idx in range(0, num_rows, chunk_size):
        # Get the chunk of rows
        chunk = data.iloc[start_idx:start_idx + chunk_size]

        # Calculate the average RGB values of the chunk
        avg_rgb = chunk[["Red", "Green", "Blue"]].mean()
        avg_r, avg_g, avg_b = avg_rgb["Red"], avg_rgb["Green"], avg_rgb["Blue"]

        # Map average RGB to pitch and volume
        brightness = (avg_r + avg_g + avg_b) / 3
        pitch = 200 + (brightness / 255) * (2000 - 200)  # Map brightness to pitch
        volume = -20 + ((avg_r + avg_g + avg_b) / (3 * 255)) * 20  # Map brightness to volume (in dB)

        # Generate tone (50ms duration for each chunk)
        tone = generate_tone(pitch, 80, volume)

        # Combine the tone with the previous sounds (if any)
        if combined_sound is None:
            combined_sound = tone
        else:
            combined_sound += tone

    # Export the combined sound to a single file
    combined_sound.export("combined_sound.wav", format="wav")
    print("Sound file 'combined_sound.wav' generated.")

if __name__ == "__main__":
    csv_file_path = "csvformat.csv"

    # Generating and combining sounds for pixel data
    generate_sounds_from_csv(csv_file_path)

files.download("combined_sound.wav")
