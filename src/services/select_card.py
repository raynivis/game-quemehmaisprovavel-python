import pandas as pd
import json
import os

def filtram_perguntas(modelo_pergunta):
    with open("services\\db.json", 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    # Carrega o JSON em um DataFrame do pandas
    df = pd.DataFrame(json_data)

    # Filtra o DataFrame com base no modelo da pergunta
    df_filtrado = df[df['Modelo da Pergunta'].isin(modelo_pergunta)]

    # Retorna a lista de perguntas filtradas
    return df_filtrado['Pergunta ("Quem e mais provavel de [Campo de Resposta]"):'].tolist()
