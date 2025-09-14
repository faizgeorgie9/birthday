import streamlit as st
from PIL import Image

# Set title of the page
st.set_page_config(page_title="Tekan Tombolnyaaa", page_icon="🎉")

if 'opened' not in st.session_state:
    st.session_state.opened = False

if not st.session_state.opened:
    # Halaman kosong dengan tombol "Open It"
    st.title("Tekan Tombolnyaaa!!!")
    st.write("Klik tombol di bawah untuk mulai...")
    if st.button("Open It"):
        st.session_state.opened = True

# Langkah 2: Halaman setelah tombol diklik
else:
    st.balloons()
    # Menampilkan gambar pertama (pacar)
    
    st.audio("luthfi-aulia-langit-favorit-official-music-video-128-ytshorts.savetube.me.mp3", format="audio/mp3", start_time=0)

    # Menampilkan foto kolase (4 foto dalam satu kolase)
    col1, col2 = st.columns(2)
    with col1:
        st.image("image1.jpg",  use_container_width=True)
    with col2:
        st.image("image7.jpg", use_container_width=True)

    col3, col4 = st.columns(2)
    with col3:
        st.image("image10.jpg",  use_container_width=True)
    with col4:
        st.image("image8.jpg", use_container_width=True)

    
    

    st.markdown("""

    ### Selamat Ulang Tahun Sayang Ke 19 Tahunnn 🥳🥳🎉🎉🎊🎊🎊🎊

    Thank you, sayang, for being the most important part of my life. 
    Aku merasa sangat bersyukur dipertemukan kamu dan melakukan setiap momen berharga bersama kamu. 
    You're not just my partner, but also my best friend who is always there when I need you the most. 

    I’m so grateful that we are walking this journey together, facing challenges and celebrating all the joys. 
    Cinta kita mungkin tidak sempurna, tapi itulah yang membuat semuanya begitu berarti. I love you more than words can say. 💖
    """)

    
    # Menampilkan gambar pertama kali ketemu
    st.image("image2.jpg", caption="Date Pertama Kita 😍😍🥰🥰", use_container_width=True)
    
    # Menampilkan cerita perjalanan pacaran
    # Menampilkan cerita perjalanan pacaran
    st.markdown("""
    #### Our Journey

    Waktu pertama kali kita ketemu, aku langsung merasa ada yang spesial dari kamu. 
    Waktu itu, aku gak pernah membayangkan kalau kita jadi sebuah couple yang saling melengkapi seperti sekarang.

    Seiring berjalannya waktu, kita  berbagi banyak kenangan memorable bersama, dan juga grow up together. 
    Every step we took has always been filled with beautiful memories and happiness, even with the challenges we've faced along the way.

    """)

    
    # Menampilkan foto kolase (4 foto dalam satu kolase)
    col1, col2 = st.columns(2)
    with col1:
        st.image("image3.jpg", use_container_width=True)
    with col2:
        st.image("image4.jpg", use_container_width=True)

    col3, col4 = st.columns(2)
    with col3:
        st.image("image5.jpg", use_container_width=True)
    with col4:
        st.image("image6.jpg", use_container_width=True)

    # Menambahkan ucapan penutup
    st.markdown("""
    Dengan semua kenangan indah yang sudah kita lalui, aku berharap kita bisa terus tumbuh bersama, saling backup, dan terus mendukung satu sama lain, apapun yang terjadi. 
    Hubungan kita mungkin sudah melalui banyak fase, tapi aku yakin kita akan terus berjalan bersama, menghadapi setiap tantangan yang ada didepan.

    Terima kasih telah menjadi yang terbaik dalam hidupku, sayang. Kamu adalah segalanya bagiku, dan aku sangat mencintaimu lebih dari yang bisa aku ungkapkan dengan kata-kata. 💖
    """)



