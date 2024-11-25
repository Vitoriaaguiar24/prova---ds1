import streamlit as st

st.title("Cadastro de Paciente - Saúde")
st.markdown("Por favor, preencha os dados abaixo para o seu cadastro.")

alt = []
ps = []
conds = []

with st.form("saúde"):
    st.header("Informações de Saúde")

    altura = st.number_input("Altura (cm)", min_value=50, max_value=250, step=1, value=170)
    peso = st.number_input("Peso (kg)", min_value=10, max_value=300, step=1, value=70)
    condições = st.text_area("Condições de Saúde", placeholder="Ex.: diabetes, hipertensão, etc.")
    
    enviado = st.form_submit_button("Enviar Cadastro")

if enviado:
    if altura:
        alt.append(altura)
    if peso:
        ps.append(peso)
    if condições:
        conds.append(condições)        
    if altura and peso and condições:
        st.success("Cadastro realizado com sucesso! Seja Bem-Vindo(a).")
    else:
        st.error("Por favor, verifique se todos os campos estão preenchidos.")