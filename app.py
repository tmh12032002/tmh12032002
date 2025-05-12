import os
import streamlit as st
from utils.player import MusicPlayer
from mutagen.mp3 import MP3


player = MusicPlayer()


song_dir = 'assets/songs/'
songs = [os.path.join(song_dir, song) for song in os.listdir(song_dir) if song.endswith('.mp3')]
song_titles = [MP3(song).tags['TIT2'].text[0] if 'TIT2' in MP3(song).tags else os.path.basename(song) for song in songs]


cover_image_dir = 'assets/images/'
cover_images = [os.path.join(cover_image_dir, image) for image in os.listdir(cover_image_dir) if image.startswith('cover_image')]
cover_images.sort()  


st.markdown("<h1 style='text-align: center;'>Music Player</h1>", unsafe_allow_html=True)


if 'current_song_index' not in st.session_state:
    st.session_state.current_song_index = 0

current_song_index = st.session_state.current_song_index


col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.write("")

with col2:
    st.image(cover_images[current_song_index], width=300)

with col3:
    st.write("")


st.write(f"Currently Playing: {song_titles[current_song_index]}")


col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    if st.button('⏮️'):
        st.session_state.current_song_index = player.prev_song(songs, current_song_index)
        
with col2:
    if st.button('▶️'):
        player.load_song(songs[current_song_index])
        player.play_song()

with col3:
    if st.button('⏸️'):
        player.pause_song()

with col4:
    if st.button('⏯️'):
        player.unpause_song()

with col5:
    if st.button('⏹️'):
        player.stop_song()

with col6:
    if st.button('⏭️'):
        st.session_state.current_song_index = player.next_song(songs, current_song_index)


st.write("Playlist:")
for idx, title in enumerate(song_titles):
    st.write(f"{idx+1}. {title}")