from gtts import gTTS
import os

def text_to_speech(text, output_file):
    tts = gTTS(text=text, lang='en')

    tts.save(output_file)

    os.system(" mpg321 " + output_file)

    #Example
input_text = "Hi my name Jayatri"
output_filename = "output.mp3"
text_to_speech(input_text, output_filename)