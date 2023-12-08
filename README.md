# ECE 469/569 Final Project
Name: Smart Device Laser Attack

Team: 9

Members: Seth Jeroutek, Matthew Bowlby, Arthur Jur

![LaserGIF](https://github.com/sethjeroutek/ECE-469-569-Final-Project/assets/132285802/b7932a50-64e2-48fd-9289-d92eba562769)

# Build
#### MATLAB folder
'conv.m' must be run inside of MATLAB.

#### src folder
This holds our code for our attempt at amplitude modulation. We ultimately did not use this.

    am.py - Usage: python am.py <audio_file> <output_file> <carrier frequency> <graph [0,1]>

This is the code used to generate our text-to-speech (TTS) lines.

    tts.py - Usage: python tts.py <text> <filename>  <rate [0-200]> <volume [0.0-1.0]> <voice [0,1]>

This serves as a high-pass filter, changing small values in the waveform presented in a CSV file to 0 to clean up the waveform.

    hpf.py - Usage: python hpf.py

    