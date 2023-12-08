import pyttsx3
import sys

def get_arguments():
    if len(sys.argv) < 6:
        print("Usage: python tts.py <text> <filename>  <rate [0-200]> <volume [0.0-1.0]> <voice [0,1]>")
        print("                            Filepath of  Words per      Quiet to loud.            0 for male")
        print("                            output file. minute.                                    1 for female")
        sys.exit(1)
    else:
        text = sys.argv[1]          # Text to get said.
        filename = sys.argv[2]      # Filename of output audio file.
        rate = sys.argv[3]          # Rate of talking.
        volume = sys.argv[4]        # Volume of talking.
        voice = sys.argv[5]         # 0 for male, 1 for female.
    
    return text, filename, rate, volume, voice

text, filename, rate, volume, voice, = get_arguments()

engine = pyttsx3.init()

engine.setProperty('rate', int(rate))               # Rate of talking.
engine.setProperty('volume', float(volume))         # Volume of talking.

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[int(voice)].id)  # Available voices.

engine.save_to_file(text, filename)
engine.runAndWait()
