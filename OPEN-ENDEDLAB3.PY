#Sampling
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from pydub import AudioSegment
sample_rate, audio_signal = wavfile.read('c:\\Users\\Nobel\\Downloads\\sample-3s.wav')
downsample_factor = 4  # Downsample by a factor of 4
downsampled_audio_signal = audio_signal[::downsample_factor]
new_sample_rate = sample_rate // downsample_factor
plt.figure(figsize=(12, 6))
plt.plot(downsampled_audio_signal, label='Downsampled Audio Signal', color='green')
plt.title('Downsampled Audio Signal in Time Domain')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.legend()
plt.show()
downsampled_audio_file = 'downsampled_audio.wav'
wavfile.write(downsampled_audio_file, new_sample_rate, downsampled_audio_signal)
audio = AudioSegment.from_wav(downsampled_audio_file)
mp3_file = 'downsampled_audio.mp3'
audio.export(mp3_file, format='mp3')
print(f'Downsampled audio saved as {mp3_file}')