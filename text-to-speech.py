

import streamlit as st
import comtypes
import pyttsx3

st.title('Text to speech App')

st.write('It is a text to speech app so you enter text in below prompt and after enter text press button you listen this')

user_input= st.text_area('Enter text here')


if st.button('Male Voice'):
    #text_to_speech = gTTS(user_input)
    #text_to_speech.save('text_to_speech_gtts.wav')
    #sound_file = 'text_to_speech_gtts.wav'
    #st.audio(sound_file,autoplay=True)
    audio = pyttsx3.init(driverName='sapi5')
    audio.setProperty('rate', 130)
    audio.setProperty('volume', 1.0)

# change the voices
    voice = audio.getProperty('voices')

# 0 for male and 1 for female
    audio.setProperty('voice', voice[0].id)      # for male voice   
#audio.setProperty('voice', voice[1].id)       # for female voice

# text-to speech conversion
    audio.say(user_input)

# save the audio file
    audio.save_to_file(user_input, 'test_male_Voice.mp3')
    #audio.save_to_file(user_input, 'test_female_Voice.mp3')

    audio.runAndWait()
    
if st.button('Female voice'):
    
    audio = pyttsx3.init(driverName='sapi5')
    audio.setProperty('rate', 150)
    audio.setProperty('volume', 1.0)

# change the voices
    voice = audio.getProperty('voices')

# 0 for male and 1 for female
    #audio.setProperty('voice', voice[0].id)      # for male voice   
    audio.setProperty('voice', voice[1].id)       # for female voice

# text-to speech conversion
    audio.say(user_input)

# save the audio file
    #audio.save_to_file(user_input, 'test_male_Voice.mp3')
    audio.save_to_file(user_input, 'test_female_Voice.mp3')

    audio.runAndWait()
