# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 18:01:44 2015
 
@author: Han Changyo
"""
 
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import os

# sampling rate
Fs = 44100.0 # Hz
 
# play length
tlen = 1 # s
Ts = 1/Fs # sampling interval
t = np.arange(0, tlen, Ts) # time array
 
# generate signal
sin_freq = 440 # Hz
signal = np.sin(2*np.pi*sin_freq*t)
 
# generate noise
noise = np.random.uniform(-1, 1, len(t))*0.1
 
# signal + noise
signal_n = signal + noise
 
# fft
signal_f = np.fft.fft(signal_n)
freq = np.fft.fftfreq(len(t), Ts)
 
# plot
plt.plot(freq, 20*np.log10(np.abs(signal_f)))
plt.xlim(0, Fs/2)
 
# save as wav file
scaled = np.int16(signal_n/np.max(np.abs(signal_n)) * 32767)
write('test.wav', 44100, scaled)
 
# play wav file
os.system("start test.wav")
