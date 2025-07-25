import streamlit as st
from gtts import gTTS
import tempfile
import os

st.set_page_config(page_title="Text-to-Speech App", layout="centered")

st.title("🗣️ Text-to-Speech Converter (2000 Words Limit)")
st.markdown("""
This app uses **Google Text-to-Speech (gTTS)** to convert your text into speech.  
Paste up to 2000 words and click "Convert to Speech".
""")

# Text input box
text_input = st.text_area("Enter your text here (max 2000 words)", height=300)

# Word count and validation
word_count = len(text_input.split())
st.write(f"**Word Count:** {word_count} / 2000")

if word_count > 2000:
    st.error("❌ Text exceeds 2000 words. Please shorten it.")
else:
    if st.button("🔊 Convert to Speech"):
        if not text_input.strip():
            st.warning("Please enter some text.")
        else:
            with st.spinner("Generating audio..."):
                tts = gTTS(text=text_input)
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                    tts.save(fp.name)
                    st.success("✅ Audio generated successfully!")
                    st.audio(fp.name, format="audio/mp3")
                    
                    # Download link
                    with open(fp.name, "rb") as audio_file:
                        audio_bytes = audio_file.read()
                        st.download_button(
                            label="⬇️ Download Audio",
                            data=audio_bytes,
                            file_name="speech.mp3",
                            mime="audio/mpeg"
                        )

