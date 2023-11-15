import pyttsx3
import sys

def get_arguments():
    if len(sys.argv) < 7:
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

engine = pyttsx3.init() # object creation

engine.setProperty('rate', int(rate))        # Rate of talking.
engine.setProperty('volume', float(volume))    # Volume of talking.

# Apply whispering effect (if available in the voice)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[int(voice)].id)  # Use the second voice, assuming it supports whispering

engine.save_to_file(text, filename)
engine.runAndWait()
