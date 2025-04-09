#import joblib
import streamlit as st
import numpy as np

# Charger le modèle
model_path = "expresso.pkl
model = joblib.load(model_path)


# Entrées utilisateur

REGION = st.number_input('Donner la region :')
MONTANT = st.number_input('Donner le montant :')
FREQUENCE = st.number_input('Donner la frequence:')
REGULARITY = st.number_input('Preciser la regularité :')
ON_NET = st.number_input('Appel passer :')



# Bouton de prédiction

if st.button("🔮 Prédire "):
    # Créer l'input pour le modèle sous forme de tableau numpy
    input_data = np.array([[REGION, MONTANT, FREQUENCE, REGULARITY, ON_NET]])

    # Faire la prédiction
    prediction = model.predict(input_data)[0]

    # Afficher le résultat
    if prediction == 1:
        st.success("✅ CHURN")
    else:
        st.error("❌ désabonnement")
