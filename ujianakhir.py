import streamlit as st
import time

# ---------------------------
# CSS untuk glitch dan animasi berkedip
# ---------------------------
st.markdown("""
<style>
/* Glitch effect untuk judul */
.glitch {
  font-weight: bold;
  font-size: 32px;
  color: white;
  position: relative;
  display: inline-block;
  user-select: none;
}
.glitch::before,
.glitch::after {
  content: attr(data-text);
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  overflow: hidden;
  clip: rect(0, 900px, 0, 0);
}
.glitch::before {
  animation: glitchTop 2s infinite linear alternate-reverse;
  color: #f0f;
  z-index: -1;
}
.glitch::after {
  animation: glitchBottom 1.5s infinite linear alternate-reverse;
  color: #0ff;
  z-index: -1;
}
@keyframes glitchTop {
  0% { clip: rect(0, 9999px, 0, 0); }
  5% { clip: rect(5px, 9999px, 10px, 0); }
  10% { clip: rect(15px, 9999px, 20px, 0); }
  15% { clip: rect(25px, 9999px, 30px, 0); }
  20% { clip: rect(35px, 9999px, 40px, 0); }
  25% { clip: rect(0, 9999px, 0, 0); }
  100% { clip: rect(0, 9999px, 0, 0); }
}
@keyframes glitchBottom {
  0% { clip: rect(40px, 9999px, 45px, 0); }
  5% { clip: rect(30px, 9999px, 35px, 0); }
  10% { clip: rect(20px, 9999px, 25px, 0); }
  15% { clip: rect(10px, 9999px, 15px, 0); }
  20% { clip: rect(0, 9999px, 5px, 0); }
  25% { clip: rect(40px, 9999px, 45px, 0); }
  100% { clip: rect(40px, 9999px, 45px, 0); }
}

/* Terminal style */
.terminal-box {
    background-color: black;
    color: #00FF00;
    font-family: 'Courier New', Courier, monospace;
    padding: 15px;
    border-radius: 10px;
    font-size: 16px;
    white-space: pre-wrap;
    min-height: 200px;
    box-shadow: 0 0 10px #00FF00;
}

/* Blink effect untuk kursor dan baris tertentu */
.blink {
    animation: blink 1s steps(1, start) infinite;
}
.blink-line {
    animation: blink 1.2s steps(1, start) infinite;
    color: #FF5722;
}

@keyframes blink {
    0%, 50% { opacity: 1; }
    51%, 100% { opacity: 0; }
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Fungsi input boolean
# ---------------------------
def boolean_input(label):
    return st.radio(f"**{label}**", ["True", "False"], horizontal=True) == "True"

# Fungsi visual kartu logika
def style_card(title, value):
    color = "#4CAF50" if value else "#F44336"
    icon = "✅" if value else "❌"
    st.markdown(f"""
        <div style="
            background: {color}22;
            border: 2px solid {color};
            border-radius: 10px;
            padding: 15px;
            margin: 10px;
            text-align: center;">
            <div style="font-size:40px;">{icon}</div>
            <h3 style="color:{color}; margin:5px 0;">{title}</h3>
            <h2 style="margin:0;">{value}</h2>
        </div>
    """, unsafe_allow_html=True)

# ---------------------------
# Judul dengan glitch effect
# ---------------------------
st.markdown('<h1 class="glitch" data-text="🧠 Evaluasi Logika Proyek Seawall">🧠 Evaluasi Logika Proyek Seawall</h1>', unsafe_allow_html=True)

# ---------------------------
# Profil Mahasiswa
# ---------------------------
st.markdown("### 👤 Profil Mahasiswa")

profile_cols = st.columns(3)

with profile_cols[0]:
    st.markdown("""
        <div style="
            background: #F0F8FF;
            border-left: 5px solid #4CAF50;
            border-radius: 8px;
            padding: 10px 15px;
            margin-bottom: 10px;">
            <h4 style="margin: 0;">Nama</h4>
            <p style="margin: 0;">Kaka Felix Amon</p>
        </div>
    """, unsafe_allow_html=True)

with profile_cols[1]:
    st.markdown("""
        <div style="
            background: #F0F8FF;
            border-left: 5px solid #2196F3;
            border-radius: 8px;
            padding: 10px 15px;
            margin-bottom: 10px;">
            <h4 style="margin: 0;">NIM</h4>
            <p style="margin: 0;">123456789</p>
        </div>
    """, unsafe_allow_html=True)

with profile_cols[2]:
    st.markdown("""
        <div style="
            background: #F0F8FF;
            border-left: 5px solid #FF9800;
            border-radius: 8px;
            padding: 10px 15px;
            margin-bottom: 10px;">
            <h4 style="margin: 0;">Kelas</h4>
            <p style="margin: 0;">Teknik Informatika 24A1</p>
        </div>
    """, unsafe_allow_html=True)

# ---------------------------
# Animasi Terminal
# ---------------------------
st.markdown("### 💻 Terminal Status")

if st.button("🟢 Tampilkan Validasi Terminal"):
    terminal_text = [
        "> INIT SYSTEM...",
        "> CHECKING MAHASISWA PROFILE",
        "> NAMA: Kaka Felix Amon",
        "> NIM: 123456789",
        "> KELAS: Teknik Informatika 24A1",
        "> VALIDATING...",
        "> STATUS: OK"
    ]

    terminal_box = st.empty()
    output = ""

    for i, line in enumerate(terminal_text):
        # Berikan kelas blink-line pada baris validasi
        if line.startswith("> VALIDATING") or line.startswith("> STATUS"):
            line_html = f'<span class="blink-line">{line}</span>'
        else:
            line_html = line

        output += line_html + "\n"
        terminal_box.markdown(
            f"""<div class="terminal-box">{output}<span class="blink">█</span></div>""",
            unsafe_allow_html=True
        )
        time.sleep(0.4)

# ---------------------------
# Gambar dan Instruksi
# ---------------------------
col_img, col_instruksi = st.columns([1.2, 1.5])
with col_img:
    st.image(
        "https://cloudfront-us-east-2.images.arcpublishing.com/reuters/NWHHR77HJ5O5BFGSSDFGLN6ALY.jpg",
        caption="Sumber: Reuters, 2025-06-12",
        use_column_width=True
    )
with col_instruksi:
    st.info("""
    Pilih nilai untuk proposisi berikut:

    - **p**: Pemerintah membangun seawall  
    - **q**: Banjir dan rob dapat dicegah  
    - **r**: Penurunan muka tanah dapat ditahan  
    - **s**: Proyek melibatkan investor asing  
    - **t**: Proyek menelan biaya $80 miliar  
    """)

# ---------------------------
# Input & Submit Form
# ---------------------------
with st.form("form_input"):
    st.markdown("## 📝 Input Proposisi Logika")
    col1, col2 = st.columns(2)
    with col1:
        p = boolean_input("p: Pemerintah membangun seawall")
        q = boolean_input("q: Banjir dan rob dapat dicegah")
        r = boolean_input("r: Penurunan muka tanah dapat ditahan")
    with col2:
        s = boolean_input("s: Proyek melibatkan investor asing")
        t = boolean_input("t: Proyek menelan biaya $80 miliar")
    
    submit = st.form_submit_button("🔍 Evaluasi Logika")

# ---------------------------
# Hasil Logika dan Narasi animasi terminal (huruf per huruf)
# ---------------------------
if submit:
    q_and_r = q and r
    implikasi = (not p) or q_and_r
    s_and_t = s and t
    final = implikasi and s_and_t

    st.markdown("## 📊 Hasil Evaluasi Logika")
    cols = st.columns(4)
    with cols[0]: style_card("q ∧ r", q_and_r)
    with cols[1]: style_card("p → (q ∧ r)", implikasi)
    with cols[2]: style_card("s ∧ t", s_and_t)
    with cols[3]: style_card("Final", final)

    st.markdown("## 📖 Narasi Logika")

    story_lines = []

    if p:
        story_lines.append("- Pemerintah **membangun seawall**.")
        if q_and_r:
            story_lines.append("  Seawall itu berhasil: **banjir dicegah dan tanah tidak turun**. ✅")
            logic1 = True
        else:
            story_lines.append("  Tapi sayangnya, **tujuan tidak tercapai sepenuhnya**. ❌")
            logic1 = False
    else:
        story_lines.append("- Pemerintah **tidak membangun seawall**.")
        story_lines.append("  Maka hubungan logikanya tetap dianggap **benar**. ✅")
        logic1 = True

    if s_and_t:
        story_lines.append("- Proyek **melibatkan investor asing dan dananya mencukupi**. ✅")
        logic2 = True
    else:
        story_lines.append("- Proyek **tidak memenuhi syarat pendanaan sepenuhnya**. ❌")
        logic2 = False

    if logic1 and logic2:
        story_lines.append("\n🎯 Kesimpulan: Proyek ini **LOGIS secara keseluruhan** ✅")
    else:
        story_lines.append("\n⚠️ Kesimpulan: Proyek ini **belum logis sepenuhnya** ❌")

    # Animasi huruf demi huruf
    story_placeholder = st.empty()
    full_text = ""

    for line in story_lines:
        for char in line:
            full_text += char
            story_placeholder.markdown(full_text)
            time.sleep(0.02)
        full_text += "\n"
