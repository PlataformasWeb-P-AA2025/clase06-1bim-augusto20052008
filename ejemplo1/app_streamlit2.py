import streamlit as st
from sqlalchemy.orm import sessionmaker
from crear_base import Saludo2
from configuracion import engine

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

# Consultar docentes
saludos = session.query(Saludo2).all()

# Mostrar con Streamlit
st.title("Presentación de Saludos")

# Mostrar saludos uno por uno
st.markdown("### Lista de saludos")
for saludo in saludos:
    st.write(saludo)

# Mostrar tabla
st.markdown("---")
st.markdown("### Tabla de saludos")

lista = []
for s in saludos:
    lista.append({
        "ID": s.id,
        "Mensaje": s.mensaje,
        "Tipo": s.tipo,
        "Origen": s.origen
    })

st.dataframe(lista)
