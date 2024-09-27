#Load and Prepare Audio Signal
import numpy as np
import matplotlib.pyplot as plt
import librosa
# Load the audio file
file_path = r'C:\Users\Nobel\Downloads\sample-3s.mp3'
audio_signal, sample_rate = librosa.load(file_path, sr=None)
# Normalize audio signal
audio_signal = audio_signal / np.max(np.abs(audio_signal), axis=0)
# Plot the original audio signal
plt.figure(figsize=(12, 6))
plt.plot(audio_signal, label='Original Audio Signal')
plt.title('Original Audio Signal in Time Domain')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.legend()
plt.show()
