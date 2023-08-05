import pyttsx3
import speech_recognition
from datetime import date,datetime
import wikipedia
import webbrowser
import os

jarvis_hear = speech_recognition.Recognizer()
Jarvis_speak = pyttsx3.init()

while True:
	with speech_recognition.Microphone() as mic:
		print("Jarvis: I'm listening")
		audio = jarvis_hear.listen(mic)
	print("Jarvis: ...")
	try:
		you = jarvis_hear.recognize_google(audio)
	except:
		you= ""
	if you=="":
		jarvis="I can't hear you"
	elif "today" in you:
		today = date.today()
		jarvis = today.strftime("%B %d, %Y")
	elif "hello" in you:
		jarvis = "Hello"
	elif "time" in you:
		now=datetime.now()
		jarvis=now.strftime("%H Hours %M Minutes")
	elif "name" in you:
		jarvis="My name is Jarvis"
	elif 'shut down' in you:
		os.system('shutdown -s')
	elif 'restart' in you:
		os.system('shutdown -r')
	elif "YouTube" in you:
		webbrowser.open('https://www.youtube.com',new=2)
		jarvis="Ok!Bye"
		rint('Me:',you)
		print('AI:',jarvis)
		Jarvis_speak = pyttsx3.init()
		Jarvis_speak.say(Jarvis)
		Jarvis_speak.runAndWait()
		break
	elif "Google" in you:
		webbrowser.open('https://www.google.com.vn/',new=2)
		jarvis="Ok!Bye"
		print('Me:',you)
		print('AI:',jarvis)
		Jarvis_speak = pyttsx3.init()
		Jarvis_speak.say(Jarvis)
		Jarvis_speak.runAndWait()
		break
	elif "music" in you:
		webbrowser.open('https://www.youtube.com/results?search_query=music',new=2)
		jarvis="Ok!Bye"
		print('Me:',you)
		print('AI:',jarvis)
		Jarvis_speak = pyttsx3.init()
		Jarvis_speak.say(Jarvis)
		Jarvis_speak.runAndWait()
		break
	elif "weather" in you:
		webbrowser.open('https://www.msn.com/vi-vn/weather/forecast/in-Th%E1%BB%91ng-Nh%E1%BA%A5t,%C4%90%E1%BB%93ng-Nai?ocid=msedgntp&cvid=932bc06f8b0e44cb8522f48f69c8f5bf&loc=eyJsIjoiVGjhu5FuZyBOaOG6pXQiLCJyIjoixJDhu5NuZyBOYWkiLCJyMiI6IlRo4buRbmcgTmjhuqV0IiwiYyI6IlZp4buHdCBOYW0iLCJpIjoiVk4iLCJ0IjoxMDIsImciOiJ2aS12biIsIngiOiIxMDcuMTU3OTk3MTMxMzQ3NjYiLCJ5IjoiMTAuOTQ4MzAwMzYxNjMzMyJ9&weadegreetype=C',new=2)
		print('Me:',you)
		print('AI:',jarvis)
		Jarvis_speak = pyttsx3.init()
		Jarvis_speak.say(Jarvis)
		Jarvis_speak.runAndWait()
		break
	elif "Facebook" in you:
		webbrowser.open('https://www.facebook.com/',new=2)
		print('Me:',you)
		print('AI:',jarvis)
		Jarvis_speak = pyttsx3.init()
		Jarvis_speak.say(Jarvis)
		Jarvis_speak.runAndWait()
		break
	elif "Gmail" in you:
		webbrowser.open('https://mail.google.com/mail/u/0/#inbox',new=2)
		print('Me:',you)
		print('AI:',jarvis)
		Jarvis_speak = pyttsx3.init()
		Jarvis_speak.say(Jarvis)
		Jarvis_speak.runAndWait()
		break
	elif "thank" in you:
		Jarvis='You are welcome'
		print('Me:',you)
		print('AI:',jarvis)
		Jarvis_speak = pyttsx3.init()
		Jarvis_speak.say(Jarvis)
		Jarvis_speak.runAndWait()
		break
	elif "bye" in you:
		Jarvis='GoodBye'
		print('Me:',you)
		print('AI:',Jarvis)
		Jarvis_speak = pyttsx3.init()
		Jarvis_speak.say(Jarvis)
		Jarvis_speak.runAndWait()
		break
	elif you=='Wikipedia':
		hear = speech_recognition.Recognizer()
		with speech_recognition.Microphone() as mic:
			print("Wikipedia: ...")
			audio = hear.listen(mic)
		try:
			wiki = hear.recognize_google(audio)
		except:
			wiki='Sorry'
		wikipedia.set_lang("vi")
		wiki=wikipedia.summary(wiki)
		print(wiki)
		Jarvis = 'Finish ^.^'
		time.sleep(3)
	else: ai='Sorry!'	
	print('Me:',you)
	print('Jarvis:',Jarvis)
	Jarvis_speak.say(Jarvis)
	Jarvis_speak.runAndWait()