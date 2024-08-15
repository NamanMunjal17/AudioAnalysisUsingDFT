import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.io import wavfile

def output(file):
    # Read the WAV file
    def read_wav_file(file_path):
        framerate, audio_samples = wavfile.read(file_path)
        audio_samples=audio_samples/np.abs(audio_samples).max()
        return audio_samples, framerate

    # Plot the waveform
    def plot_waveform(audio_samples, framerate, title="Waveform"):
        time_axis = np.linspace(0, len(audio_samples) / framerate, num=len(audio_samples))
        return time_axis,audio_samples

    # Example usage
    audio_samples, framerate = read_wav_file(file)
    # If the audio is stereo, you might want to take one channel for plotting
    if audio_samples.ndim == 2:
        audio_samples = audio_samples[:, 0]  # Take the first channel

    #plot_waveform(audio_samples, framerate, title="Waveform of example.wav")
    global mags
    mags=[]
    def wrap(freq,audio_samples,framerate):
        global mags
        wrapX,wrapY=[],[]
        for i in range(0,len(audio_samples)):
            t=i/framerate
            angle=2*math.pi*freq*t
            x,y=-math.cos(angle)*audio_samples[i],math.sin(angle)*audio_samples[i]
            wrapX.append(x)
            wrapY.append(y)
        #plt.clf()
        #plt.scatter(wrapX,wrapY)
        comx,comy=sum(wrapX)/len(wrapX),sum(wrapY)/len(wrapY)
        mag=math.sqrt(comx**2+comy**2)
        mags.append(mag)
        #plt.pause(0.01)

    for i in range(1000):
        wrap(i,audio_samples,framerate)
    x_values = np.linspace(0, len(mags) - 1, len(mags))
    return x_values,mags,plot_waveform(audio_samples,framerate)[0],plot_waveform(audio_samples,framerate)[1]