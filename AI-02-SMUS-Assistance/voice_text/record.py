import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

def voice(filename, duration=5, fs=44100):
    print('Recording...')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    print('Recording done')
    wav.write(filename, fs, myrecording)