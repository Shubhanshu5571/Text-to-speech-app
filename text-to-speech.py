

from gtts import gTTS
import streamlit as st


st.title('Text to speech App')

st.write('It is a text to speech app so you enter text in below prompt and after enter text press button you listen this')

user_input= st.text_area('Enter text here')

if st.button("Convert to Speech"):
    if user_input:
         
        # Convert text to speech
        tts = gTTS(user_input, lang='en')

        # Save the converted audio to a file
        tts.save("text_to_speech_gtts.wav")

        # Play the audio file in the Streamlit app
        audio_file = 'text_to_speech_gtts.wav'
        st.audio(audio_file, format="audio/wav",autoplay=True)
    else:
        st.warning("Please enter some text.")
