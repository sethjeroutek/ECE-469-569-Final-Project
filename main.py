import numpy as np
import matplotlib.pyplot as plt
import sys
import csv
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

# Get command-line arguments.
def get_arguments():
    if len(sys.argv) < 4:
        print("Usage: python main.py <audio_file> <output_file> <k> <carrier frequency> <graph [0,1]>")
        print("                      Filepath of   'graph' must                                 0 to print output to .csv file.")
        print("                      audio file.   be 1.                                          1 to graph output.")
        sys.exit(1)
    else:
        argument = sys.argv[1]
        output = sys.argv[2]
        k = int(sys.argv[3])
        c_freq = float(sys.argv[4])
        graph = int(sys.argv[5])

    return argument, output, k, c_freq, graph

# Get the modulating signal from input.
def get_modulating_signal(audio_file):
    sampling_rate, data = wavfile.read(audio_file)
    if len(data.shape) == 2:
            data = data.mean(axis=1)

    return sampling_rate, data

# Read in from command line.
audio_file, output, k, c_freq, graph = get_arguments()

sampling_rate, data = get_modulating_signal(audio_file)
duration = data.shape[0] / sampling_rate
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Create carrier and information signals.
carrier = np.cos(2 * np.pi * c_freq * t)
information = data / max(data)

# Perform AM modulation.
am_modulated_signal = (1 + (k * information)) * carrier

if (graph == 1): 
    graph_signals([carrier, am_modulated_signal, information], t)
else:
    # Organize waveform into time and voltage columns.
    data = np.column_stack((t, am_modulated_signal))

    # Save the data to a CSV file.
    np.savetxt(output, data, delimiter=',', comments='')