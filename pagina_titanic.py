## Ivan morales 2/23/24

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
path='ivanmorales22/streamlit/test.csv'
df=pd.read_csv(path)

males=df[(df['Sex'] == 'male')]
females=df[(df['Sex'] == 'female')]

st.title('Analisis de Database del titanic')
st.header('Analisis mediante Histogramas por Variable')

#Mostramos el histograma de la division de pasajeros por sexo
st.subheader('Cantidad de Pasajeros masculinos y femeninos')
fig, ax = plt.subplots()
ax.hist(df['Sex'], bins=2, edgecolor='black')
ax.set_xlabel('Gender')
ax.set_ylabel('Cantidad de Pasajeros')

st.pyplot(fig)

#Mostramos el histograma de la division de pasajeros por si sobrevivio o no
st.subheader('Cantidad de Pasajeros que sobrevivieron vs que no sobrevivieron')
fig, ax = plt.subplots()
ax.hist(df['Survived'], bins=2, edgecolor='black')
ax.set_xlabel('Sobrevivio')
ax.set_ylabel('Cantidad de Pasajeros')
custom_labels = ['No', 'Sí']
ax.set_xticks([0, 1])
ax.set_xticklabels(custom_labels)
st.pyplot(fig)

#Mostramos el histograma de la division de pasajeros de acuerdo a las clases
st.subheader('Cantidad de Pasajeros por Clase')
fig, ax = plt.subplots()
ax.hist(df['Pclass'], bins=3, edgecolor='black')
ax.set_xlabel('Clase')
ax.set_ylabel('Cantidad de Pasajeros')
custom_labels = ['1era Clase', '2da Clase', '3era Clase']
ax.set_xticks([1, 2, 3])
ax.set_xticklabels(custom_labels)

st.pyplot(fig)

#Mostramos el histograma de la representacion de las edades
st.subheader('Cantidad de Pasajeros por edad')
fig, ax = plt.subplots()
ax.hist(df['Age'], bins=20, edgecolor='black')
ax.set_xlabel('Edad')
ax.set_ylabel('Cantidad de Pasajeros')

st.pyplot(fig)

#Mostramos el histograma de la representacion de la cantidad de Parch
st.subheader('Cantidad de Parchs')
st.write('Parch indica el numero de Padres e hijos a bordo')
fig, ax = plt.subplots()
ax.hist(df['Age'], bins=8, edgecolor='black')
ax.set_xlabel('Parents/children')
ax.set_ylabel('Cantidad de Parch')

st.pyplot(fig)
