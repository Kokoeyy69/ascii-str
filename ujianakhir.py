# pylint: disable=no-member
import streamlit as st
import time
import pandas as pd

# ---------------------------
# CSS Glitch + Terminal Style + Blink
# ---------------------------
st.markdown("""
<style>
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
.terminal-box {
    background-color: black;
    color: #00FF00;
    font-family: 'Courier New', Courier, monospace;
    padding: 15px;
    border-radius: 10px;
    font-size: 15px;
    white-space: pre-wrap;
    box-shadow: 0 0 10px #00FF00;
    margin-bottom: 15px;
}
.blink {
    animation: blink 1s steps(1, start) infinite;
}
@keyframes blink {
    0%, 50% { opacity: 1; }
    51%, 100% { opacity: 0; }
}
.result-card {
    background: #111;
    border-radius: 12px;
    padding: 15px;
    margin: 10px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Judul Glitch
# ---------------------------
st.markdown('<h1 class="glitch" data-text="🤖 Evaluasi Logika Proyek Seawall">🤖 Evaluasi Logika Proyek Seawall</h1>', unsafe_allow_html=True)

# ---------------------------
# Inisialisasi Session State
# ---------------------------
if "show_proposition" not in st.session_state:
    st.session_state.show_proposition = False
if "terminal_output" not in st.session_state:
    st.session_state.terminal_output = ""

# ---------------------------
# Placeholder terminal
# ---------------------------
terminal_placeholder = st.empty()

# ---------------------------
# Tombol validasi terminal
# ---------------------------
if not st.session_state.show_proposition:
    if st.button("🟢 Tampilkan Validasi Terminal"):
        ascii_logo = r"""
____________________
|  _____ ___ ____  |
|  |     |   |  |  |
|  |     |   |  |  |
|  |  ___|   |  |  |
|  |     |   |  |  |
|  |     |   |  |  |
|            |  |  |
|  |_____|__ |  |  |
|==================|
|   INFORMATIKA    |
|==================|
"""
        logo_frames = [
            ascii_logo,
            r"   [¬º-°]¬",
            r"   [¬º-°]¬ *",
            r" * [¬º-°]¬ *",
            r" * [¬º-°]¬"
        ]
        terminal_text = [
            "> INIT SYSTEM...",
            "> HABIB FATIH ZANJABILAH",
            "> TEKNIK INFORMATIKA 24A1",
            "> 312410135",
            "> ASCII LOGO LOADED",
            "> VALIDATING...",
            "> STATUS: OK",
            "> LOGIN: SUCCESS"
        ]
        output = ""

        for frame in logo_frames:
            terminal_placeholder.markdown(f"""<div class="terminal-box">{frame}<span class="blink">█</span></div>""", unsafe_allow_html=True)
            time.sleep(0.5)

        for line in terminal_text:
            if "> VALIDATING" in line or "> STATUS" in line:
                line_html = f'<span style="color:#FF5722">{line}</span>'
            else:
                line_html = line
            output += line_html + "\n"
            terminal_placeholder.markdown(f"""<div class="terminal-box">{output}<span class="blink">█</span></div>""", unsafe_allow_html=True)
            time.sleep(0.4)

        st.session_state.show_proposition = True
        st.session_state.terminal_output = output

# ---------------------------
# Render ulang terminal jika sudah pernah tampil
# ---------------------------
if st.session_state.show_proposition and st.session_state.terminal_output:
    terminal_placeholder.markdown(f"""<div class="terminal-box">{st.session_state.terminal_output}<span class="blink">█</span></div>""", unsafe_allow_html=True)

# ---------------------------
# Fungsi input boolean dengan radio
# ---------------------------
def boolean_input(label):
    return st.radio(f"**{label}**", ["True", "False"], horizontal=True) == "True"

# ---------------------------
# Fungsi efek mengetik
# ---------------------------
def typing_effect(placeholder, text, speed=0.02):
    displayed = ""
    for char in text:
        displayed += char
        placeholder.markdown(displayed)
        time.sleep(speed)
    return displayed

# ---------------------------
# Fungsi styling kartu hasil evaluasi
# ---------------------------
def style_card(title, value):
    color = "#4CAF50" if value else "#F44336"
    icon = "✅" if value else "❌"
    st.markdown(f"""
        <div class="result-card" style="background: {color}22; border: 2px solid {color};">
            <div style="font-size:40px;">{icon}</div>
            <h3 style="color:{color}; margin:5px 0;">{title}</h3>
            <h2 style="margin:0;">{value}</h2>
        </div>
    """, unsafe_allow_html=True)

# ---------------------------
# Fungsi generate tabel kebenaran otomatis
# ---------------------------
def generate_truth_table(variables, formula_func):
    from itertools import product
    rows = []
    for values in product([False, True], repeat=len(variables)):
        context = dict(zip(variables, values))
        try:
            result = formula_func(**context)
        except Exception:
            result = None
        rows.append({**context, "Formula": result})
    return pd.DataFrame(rows)

# ---------------------------
# Jika sudah validasi, tampilkan konten utama
# ---------------------------
if st.session_state.show_proposition:
    st.markdown("## 🧠 Input Tipe Proposisi Atomik (Contoh simbolik: ¬, ∧, ∨, →, ↔)")
    col1, col2 = st.columns(2)
    with col1:
        p_type = st.text_input("Tipe p (misal: kontingensi, tautologi, kontradiksi)", placeholder="")
        q_type = st.text_input("Tipe q", placeholder="")
        r_type = st.text_input("Tipe r", placeholder="")
    with col2:
        s_type = st.text_input("Tipe s", placeholder="")
        t_type = st.text_input("Tipe t", placeholder="")

    st.markdown("---")
    col1, col2 = st.columns([2, 1])
    with col1:
        # Ganti sesuai dengan file gambarmu, pastikan gambar ada di folder yg sama
        try:
            st.image("tgs.jpeg", caption="Sumber: Reuters, 2025-06-12", use_container_width=True)
        except Exception as e:
            st.error(f"Gagal memuat gambar: {e}")

    with col2:
        instruksi_lines = [
            "🧠 Pilih nilai untuk proposisi berikut:\n",
            "- **p**: Pemerintah membangun seawall",
            "- **q**: Banjir dan rob dapat dicegah",
            "- **r**: Penurunan muka tanah dapat ditahan",
            "- **s**: Proyek melibatkan investor asing",
            "- **t**: Proyek menelan biaya $80 miliar"
        ]
        instruksi_box = st.empty()
        typed = ""
        for line in instruksi_lines:
            for char in line:
                typed += char
                instruksi_box.markdown(f"""<div style="background-color:#0b2239; padding:15px; border-radius:10px; color:white; font-size:16px;">{typed}</div>""", unsafe_allow_html=True)
                time.sleep(0.01)
            typed += "\n"

    # Form input proposisi logika
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

        # Narasi logika dengan typing effect
        st.markdown("## 📖 Narasi Logika")
        story_placeholder = st.empty()
        story_lines = []

        if p:
            story_lines.append("- Pemerintah **membangun seawall**.")
            if q_and_r:
                story_lines.append("  Seawall berhasil: **banjir dicegah dan tanah tidak turun**. ✅")
                logic1 = True
            else:
                story_lines.append("  Tapi, **tujuan tidak tercapai sepenuhnya**. ❌")
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

        full_text = ""
        for line in story_lines:
            full_text = typing_effect(story_placeholder, full_text + line + "\n")

        # Kesimpulan dan penjelasan dengan efek mengetik
        conclusion_placeholder = st.empty()
        if logic1 and logic2:
            conclusion_text = ("\n🎯 Kesimpulan: Proyek ini **LOGIS secara keseluruhan** ✅\n\n"
                               "Penjelasan: Berdasarkan nilai proposisi yang dipilih, semua kondisi utama terpenuhi, "
                               "menandakan bahwa hubungan logika proyek ini konsisten dan masuk akal untuk dilanjutkan.")
        else:
            conclusion_text = ("\n⚠️ Kesimpulan: Proyek ini **belum logis sepenuhnya** ❌\n\n"
                               "Penjelasan: Ada beberapa proposisi yang tidak terpenuhi, sehingga perlu evaluasi lebih lanjut "
                               "agar proyek bisa menjadi logis dan layak secara teknis dan finansial.")

        typing_effect(conclusion_placeholder, conclusion_text)

        # Tabel kebenaran
        st.markdown("## 📋 Tabel Kebenaran Proposisi Majemuk")

        def formula(p, q, r, s, t):
            return ((not p) or (q and r)) and (s and t)

        variables = ['p', 'q', 'r', 's', 't']
        df_truth = generate_truth_table(variables, formula)
        st.dataframe(df_truth, use_container_width=True)
