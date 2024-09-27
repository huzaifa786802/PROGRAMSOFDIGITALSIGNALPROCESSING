#Filtering
import numpy as np
import matplotlib.pyplot as plt
import librosa
from scipy.signal import butter, lfilter
file_path = r'C:\Users\Nobel\Downloads\sample-3s.mp3'
audio_signal, sample_rate = librosa.load(file_path, sr=None)
audio_signal = audio_signal / np.max(np.abs(audio_signal), axis=0)
def butter_lowpass(cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a
def lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y
cutoff_frequency = 3000  # Cutoff frequency in Hz
order = 6
# Apply the filter
filtered_audio_signal = lowpass_filter(audio_signal, cutoff_frequency, sample_rate, order)
# Plot the filtered audio signal
plt.figure(figsize=(12, 6))
plt.plot(filtered_audio_signal, label='Filtered Audio Signal', color='orange')
plt.title('Filtered Audio Signal in Time Domain')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.legend()
plt.show()