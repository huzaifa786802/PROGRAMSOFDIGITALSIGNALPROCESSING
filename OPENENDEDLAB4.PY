#Visualize and Analyze
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
import soundfile as sf
def plot_frequency_spectrum(signal, sample_rate, title):
    N = len(signal)
    T = 1.0 / sample_rate
    yf = fft(signal)
    xf = fftfreq(N, T)[:N//2]
    plt.figure(figsize=(12, 6))
    plt.plot(xf, 2.0/N * np.abs(yf[:N//2]))
    plt.title(title)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.show()
audio_file = r'C:\Users\Nobel\Downloads\sample-3s.mp3'  
audio_signal, sample_rate = sf.read(audio_file)
filtered_audio_signal = audio_signal * 0.5
downsample_factor = 2
downsampled_audio_signal = audio_signal[::downsample_factor]
plot_frequency_spectrum(audio_signal, sample_rate, 'Original Audio Signal in Frequency Domain')
plot_frequency_spectrum(filtered_audio_signal, sample_rate, 'Filtered Audio Signal in Frequency Domain')
new_sample_rate = sample_rate // downsample_factor
plot_frequency_spectrum(downsampled_audio_signal, new_sample_rate, 'Downsampled Audio Signal in Frequency Domain')
plt.figure(figsize=(12, 8))
plt.plot(audio_signal, label='Original Audio Signal')
plt.plot(filtered_audio_signal, label='Filtered Audio Signal', color='orange')
plt.plot(np.arange(0, len(downsampled_audio_signal) * downsample_factor, downsample_factor),
         downsampled_audio_signal, label='Downsampled Audio Signal', color='green')
plt.title('Comparison of Audio Signals in Time Domain')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.legend()
plt.show()