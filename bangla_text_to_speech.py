from gtts import gTTS
from playsound import playsound
import os

text = "টেকনোলজি শিখি আরও সহজে!"

output = gTTS(text = text, lang = 'bn', slow=True)
output.save("output.mp3")

playsound("output.mp3")
os.remove("output.mp3")