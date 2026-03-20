import streamlit as st
import pandas as pd
from src.processor import get_stats  # On importe tes fonctions de calcul

# --- Configuration de l'interface ---
st.set_page_config(page_title="CSV Analyst", layout="wide")
st.title("📊 CSV Analyst")

# --- Barre latérale (Sidebar) pour l'import ---
with st.sidebar:
    st.header("Installation")
    # C'est ICI que le bouton magique apparaît
    uploaded_file = st.file_uploader("Importer un fichier CSV", type="csv")
    
    st.markdown("---")
    st.info("💡 Chargez un fichier pour débloquer l'analyse.")

# --- Logique d'affichage ---
if uploaded_file is not None:
    # 1. Lire le fichier dès qu'il est choisi
    df = pd.read_csv(uploaded_file)
    
    # 2. Afficher le succès
    st.success(f"Fichier '{uploaded_file.name}' chargé avec succès !")
    
    # 3. Ton tableau interactif avec scroll
    st.subheader("🧐 Aperçu des données")
    rows = st.slider("Nombre de lignes à voir", 5, len(df), 10)
    st.dataframe(df.head(rows), use_container_width=True)

    # 4. Tes stats (via ton fichier processor.py)
    st.subheader("📈 Statistiques automatiques")
    st.write(df.describe())

else:
    # Ce qui s'affiche tant qu'aucun fichier n'est choisi
    st.warning("Veuillez importer un fichier CSV depuis la barre latérale pour commencer.")