import requests
from gtts import gTTS
import os


"""A function that takes the input from user converts it to a desired alnguage and saves the speech conversion file as .mp3 file in your system."""
#uses the gTTS text to speech API

def convert(text):
	a = 'http://transltr.org/api/translate?text='+text+'&to='+'hi'+'&from='+'en'   #converting from english(en) to hindi(hi). This can be changes from here.
	r = requests.get(a)
	b = r.json()
	c = b['translationText']
	tts = gTTS(c, lang='hi')
	os.remove("/home/meghna/Desktop/mp3s/a.mp3")
	tts.save("/home/meghna/Desktop/mp3s/a.mp3")   #Specify the location where you want to save the mp3 file.
	return c

if __name__ == '__main__':
	convert("Hello")