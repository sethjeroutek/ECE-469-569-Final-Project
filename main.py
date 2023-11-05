import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy.io import wavfile

# Plots the carrier, information, and modulated signals.
def graph_signals(signals: list, t: np.array, titles=["Carrier Signal", "Information/AM Signals"]):
    plt.figure(figsize=(15, 10))

    plt.subplot(2, 1, 1)
    plt.title(titles[0])
    plt.plot(t, signals[0])

    plt.subplot(2, 1, 2)
    plt.title(titles[1])
    plt.plot(t, signals[1])
    plt.plot(t, signals[2])
    plt.legend(['AM Signal', 'Original Signal'])

    plt.xlabel("Time (s)")
    plt.show()

# Get the modulating signal from input.
def get_modulating_signal():
    # Check the number of command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python script.py <argument>")
    else:
        argument = sys.argv[1]
    
    sampling_rate, data = wavfile.read(argument)
    if len(data.shape) == 2:
            data = data.mean(axis=1)

    return sampling_rate, data

# Read in signal from command line.
sampling_rate, data = get_modulating_signal()
duration = data.shape[0] / sampling_rate
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Create carrier and information signals.
carrier = np.cos(2 * np.pi * 1000 * t)
information = data / max(data)

# Perform AM modulation.
k = 50
am_modulated_signal = (1 + (k * information)) * carrier

graph_signals([carrier, am_modulated_signal, information], t)
