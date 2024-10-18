# -------------------#
# EINRICHTUNG
import streamlit as st
import pandas as pd
from pathlib import Path

# -------------------#
# PFADE VORBEREITEN

# Ermittle das Verzeichnis des aktuellen Skripts
script_dir = Path(__file__).parent

# Konstruiere den Pfad zur CSV-Datei
data_path = script_dir.joinpath("data", "oecd.csv") 
# Konstruiere den Pfad zur Bilddatei
image_path = script_dir.joinpath("img", "hdm-logo.jpg") 

# -------------------#
# DATEN IMPORTIEREN

df = pd.read_csv(data_path)


### -------------------###
# START UNSERER APP

# -------------------#
# KOPFZEILE

# Titel unserer App
st.title("👋 Hallo, Streamlit!")


# Bild hinzufügen (wir verwenden str (String), um den Bildpfad in einen String umzuwandeln)



# -------------------#
# SEITENLEISTE

# Überschrift in Seitenleiste einfügen

# Schieberegler oder anderes Element einfügen


# -------------------#
# HAUPTTEIL

# DataFrame anzeigen




### -------------------###
# ENDE DER APP