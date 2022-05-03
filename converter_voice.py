import speech_recognition as sr
import html

# Obtém o arquivo de áudio
from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "audio_teste.wav")

# Usa o arquivo de áudio como fonte de áudio.
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # lê todo arquivo de áudio

# Reconhecimento de fala usando Google Speech Recognition
def tradutor ():
    try:
        resposta = ("Você disse :"+ r.recognize_google(audio, language="pt-BR"))
        html.unescape(resposta)
        print(resposta)
    except sr.UnknownValueError:
        print("o reconehcimento do google speech falhou")
    except sr.RequestError as e:
        print("Não foi possível achar resultados para o áudio na google speech {0}".format(e))

tradutor()