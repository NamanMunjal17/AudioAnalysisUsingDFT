from scipy.io import wavfile
import numpy as np

# Define parameters
sample_rate = 8000  # Sample rate in Hz
duration = 1  # Duration of the audio in seconds
frequency = 440  # Frequency of the sine wave in Hz

# Generate a sine wave as an example
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
audio_samples = 0.5 * np.sin(2 * np.pi * frequency * t)

audio_samples = np.int16(audio_samples * 32767)

# Write the WAV file
wavfile.write('output.wav', sample_rate, audio_samples)
