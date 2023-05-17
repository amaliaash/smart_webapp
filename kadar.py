import streamlit as st

def show_pengertian_kadar():
    st.header("Pengertian Kadar")
    st.write("Kadar analit merupakan kandungan zat yang diukur dalam suatu sampel kimia. Metode analisis kuantitatif umum digunakan untuk menentukan kadar analit yang melibatkan pengukuran jumlah zat tertentu dalam sampel dan penerapan hukum kimia untuk menghitung konsentrasinya.")

def show_rumus_kadar():
    st.header("Rumus Kadar")
    st.write("Konsentrasi terukur x Volume Labu takar x Faktor pengenceran / Bobot sampel")

def hitung_kadar(concentration, volume, dilution_factor, weight, unit):
    if dilution_factor:
        kadar = (concentration * volume * dilution_factor) / weight
    else:
        kadar = (concentration * volume) / weight
    
    if unit == "mg/L":
        kadar = kadar * 1000
    elif unit == "mg/Kg":
        kadar = kadar
    
    return kadar

st.title("Aplikasi Menghitung Kadar Sampel")

show_pengertian = st.checkbox("Pengertian Kadar")
if show_pengertian:
    show_pengertian_kadar()

show_rumus = st.checkbox("Rumus Kadar")
if show_rumus:
    show_rumus_kadar()

concentration = st.number_input("Masukkan konsentrasi (dalam ppm): ", min_value=0.0, step=0.1)
volume = st.number_input("Masukkan volume labu takar (dalam L): ", min_value=0.0, step=0.1)
dilution_factor = st.number_input("Masukkan faktor pengenceran (dalam angka): ", min_value=0.0, step=0.1, value=1.0)
weight = st.number_input("Masukkan bobot sampel (dalam gram): ", min_value=0.0, step=0.0001, format="%.4f")

unit = st.selectbox("Pilih satuan:", ("mg/L", "mg/Kg"))
st.write("NOTE: Untuk sample padat gunakan satuan mg/Kg dan Untuk sample cair gunakan satuan mg/L.")

button_style = """
    <style>
    .stButton>button {
        background-color: #FF6347;
        color: white;
        font-weight: bold;
        padding: 0.6em 1.5em;
        border-radius: 0.3em;
        border: none;
    }
    </style>
    """
st.markdown(button_style, unsafe_allow_html=True)

if st.button("Hitung Kadar Analit"):
    kadar = hitung_kadar(concentration, volume, dilution_factor, weight, unit)
    st.write("Kadar sampel adalah {:.2f} {}".format(kadar, unit))
