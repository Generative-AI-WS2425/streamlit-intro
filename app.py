# -------------------#
# EINRICHTUNG
import streamlit as st
import pandas as pd
import altair as alt
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


# Füge Bild hinzu (wir verwenden str (String), um den Bildpfad in einen String umzuwandeln)


# Füge Überschrift hinzu


# -------------------#
# SEITENLEISTE

# Überschrift

# Erstelle einen Schieberegler

# Zeige die Ausgabe der Schiebereglerauswahl an

# -------------------#
# HAUPTTEIL

# Zeige statischen DataFrame an

# Erstelle ein Diagramm mit Altair



# Zeige Diagramm an

### -------------------###
# ENDE DER APP