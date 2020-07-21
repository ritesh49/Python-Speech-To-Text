import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

def silence_based_conversion(path="alice-medium.wav"):
    song=AudioSegment.from_wav(path)

    fh=open("recognized.txt",'w+')

    chunks=split_on_silence(song,
    min_silence_len=500,
    silence_thresh=-16
    )
    try:
        os.mkdir('audio_chunks')
    except(FileExistsError):
        pass
    os.chdir('audio_chunks')

    i=0
    for chunk in chunks:
        chunk_silent=AudioSegment.silent(duration=10)
        audio_chunk=chunk_silent + chunk+ chunk_silent

        print('Saving chunk {0}.wav'.format(i))

        audio_chunk.export("./chunk{0}.wav".format(i),bitrate='192k',format='wav')
        filename='chunk'+str(i)+'.wav'
        file=filename
        r=sr.Recognizer()
        with sr.AudioFile(file) as source:
            r.adjust_for_ambient_noise(source)
            audio_listened=r.listen(source)
        try:
            rec=r.recognize_google(audio_listened)
            fh.write(rec+'. ')
        except sr.UnknownValueError:
            print('Could not understand audio')
        except sr.RequestError as e:
            print('Could not request results. check your internet connection')
        i+=1
    os.chdir('..')
if __name__ =='__main__':
    print('Enter the audio file path')
    path=input('Enter file path:  ')
    silence_based_conversion(path)

