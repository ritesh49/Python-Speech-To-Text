import speech_recognition as sr
import pyttsx3

r=sr.Recognizer()

def SpeakText(command):
    engine=pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
while(1):
    try:
        print('Say Something Now!!')
        print('line 1')
        with sr.Microphone() as source2:
            print('line 2')
            r.adjust_for_ambient_noise(source2,duration=0.2)
            print('line 3')
            audio2=r.listen(source2)
            print('line 4')
            MyText=r.recognize_google(audio2)
            print('line 5')
            MyText=MyText.lower()

            print('Did you say '+MyText)
            print('line 6')
            SpeakText(MyText)
    except sr.RequestError as e:
        print('Could not request results; {0}'.format(e))
    except sr.UnknownValueError:
        print('Could not understand what you said')