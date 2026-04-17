import streamlit as st

st.title("🏠 Smart Energy Advisor")

nb_lamps = st.number_input("Nombre de lampes", 0, 50, 5)
type_lamps = st.selectbox("Type de lampes", ["LED", "Non LED"])

ac_class = st.selectbox("Classe climatiseur", ["A", "B"])

hours = st.slider("Heures utilisation / jour", 1, 24, 5)

price_kwh = 0.2

P_current = 0
P_new = 0

# Lampes
if type_lamps == "Non LED":
    P_current += nb_lamps * 60
    P_new += nb_lamps * 10
else:
    P_current += nb_lamps * 10
    P_new += nb_lamps * 10

# AC
if ac_class == "B":
    P_current += 1500
    P_new += 900
else:
    P_current += 900
    P_new += 900

# Energie
E_current = (P_current/1000) * hours
E_new = (P_new/1000) * hours

# Cost
cost_current = E_current * price_kwh
cost_new = E_new * price_kwh

gain = cost_current - cost_new

st.subheader("📊 Résultats")

st.write("Consommation actuelle:", round(E_current,2), "kWh")
st.write("Après optimisation:", round(E_new,2), "kWh")

st.write("💰 Coût actuel:", round(cost_current,2), "DT")
st.write("💰 Nouveau coût:", round(cost_new,2), "DT")

st.success(f"💸 Gain: {round(gain,2)} DT / jour")

if type_lamps == "Non LED":
    st.warning("👉 Remplacer les lampes par LED")

if ac_class == "B":
    st.warning("👉 Utiliser climatiseur classe A")
