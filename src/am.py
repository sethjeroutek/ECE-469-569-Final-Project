import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy.io import wavfile
from scipy.signal import hilbert

# Plots the carrier, information, and modulated signals.
def graph_signals(signals: list, t: np.array, titles=["Carrier Signal", "Information/AM Signals"]):
    plt.figure(figsize=(15, 10))

    plt.subplot(2, 1, 1)
    plt.title(titles[0])
    plt.plot(t, signals[0])

    plt.subplot(2, 1, 2)
    plt.title(titles[1])
    plt.plot(t, signals[1])
    #plt.plot(t, signals[2])
    plt.legend(['AM Signal', 'Original Signal'])

    plt.xlabel("Time (s)")
    plt.show()

# Get command-line arguments.
def get_arguments():
    if len(sys.argv) < 4:
        print("Usage: python am.py <audio_file> <output_file> <carrier frequency> <graph [0,1]>")
        print("                     Filepath of  'graph' must                             0 to print output to .csv file.")
        print("                     audio file.  be 1.                                      1 to graph output.")
        sys.exit(1)
    else:
        argument = sys.argv[1]
        output = sys.argv[2]
        c_freq = float(sys.argv[3])
        graph = int(sys.argv[4])

    return argument, output, c_freq, graph

# Get the modulating signal from input.
def get_modulating_signal(audio_file):
    sampling_rate, data = wavfile.read(audio_file)
    if len(data.shape) == 2:
            data = data.mean(axis=1)

    return sampling_rate, data

# Read in from command line.
audio_file, output, c_freq, graph = get_arguments()

sampling_rate, data = get_modulating_signal(audio_file)
duration = data.shape[0] / sampling_rate
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

#t = np.arange(0, len(data) / sampling_rate, 1 / sampling_rate)

# Create carrier and information signals.

#information = (data / np.max(np.abs(data)))
#analytic = hilbert(information)
#carrier = np.abs(analytic) * np.cos(2 * np.pi * c_freq * t)
carrier = np.cos(2 * np.pi * c_freq * t)

#k = 0.9 * (k / np.max(np.abs(k)))

#information = np.cos(2 * np.pi * 5 * t)

# Perform AM modulation.
am_modulated_signal = (1 + (0.5 * data)) * carrier

#am_modulated_signal = am_modulated_signal / max(am_modulated_signal)

if (graph == 1): 
    graph_signals([carrier, am_modulated_signal, data], t)
else:
    # Organize waveform into column of data.
    data = np.column_stack(am_modulated_signal)

    # Save the data to a CSV file.
    np.savetxt(output, data, delimiter=',', comments='')