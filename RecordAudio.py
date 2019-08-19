import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  # Sample rate
seconds = 1500  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2,dtype='float64',blocking=True)
sd.wait()
write('output.wav', fs, myrecording) 
