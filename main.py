import speech_recognition as sr
import pyautogui
import pyaudio
import sys
import os
import numpy as np
import pyttsx3
from pynput. keyboard import Key, Controller
import time
import whisper
import discord_bot as bot

discordBotOn = True
voiceAssistantOn = False

if discordBotOn:
    if __name__ == '__main__':
        bot.run_discord_bot()


if voiceAssistantOn:
    # initialisation
    r = sr.Recognizer()
    index = 0
    model = whisper.load_model("base")
    micList = sr.Microphone.list_microphone_names()
    print("--------------------------")
    for i in micList:
        print(str(index) + ": " + i)
        index += 1
    print("type the number of your mic")
    print("--------------------------")
    micChoice = int(input())
    print("--------------------------")
    print("'" + micList[micChoice] + "' has been chosen")
    print("--------------------------")
    mic = sr.Microphone(device_index=micChoice)
    print("Aico Activated")

    #macro stuff
    miningMacro = False
    controls = Controller()


    # system loop
    while True:
        try:
            with mic as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source, timeout=2)
                input = r.recognize_google(audio)
                print(input)
        except sr.UnknownValueError:
            #print("not understandable")
            pass
        except sr.WaitTimeoutError:
            #print("Wait Timeout Error")
            pass
        except sr.RequestError as e:
            print(e)





    def transcribe(input:str):
        #generate audio file from input to input.wav

        #transcribe audio file
        result = model.transcribe("input.wav")

        #highlight important words 
        #and put double square brackets around words that equal file names

        #save as markdown file in obsidian vault
        pass