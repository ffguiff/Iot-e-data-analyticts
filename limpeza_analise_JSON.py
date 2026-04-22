import pandas as pd  
import json

#carregar o aquivo JSON

with open('pesagens_sensor.json') as f:
    data = json.load(f)

# "achatar" o JSON para virar uma tabela comum
df = pd.json_normalize(data)

# print(df.columns)

#limpar linhas com status diferente de "sucesso"
df = df[df['status'] == 'sucesso']

#Padronizador de pesagens
def padronizar_peso(row):
    if row['dados_tecnicos.unidade'] == 'g':
        return row ['dados_tecnicos.valor']/1000
    return row['dados_tecnicos.valor']

df['peso_final_kg'] = df.apply(padronizar_peso, axis=1)

print("Tabala limpa e padronizada:")
colunas_selecionadas = [
    '_comment',
    'status',
    'dados_tecnicos.lote',
    'dados_tecnicos.produto',
    'peso_final_kg'
]
print(df[colunas_selecionadas])

# Exportar para CSV (mais leve e rápido para o Power BI)
# exporção do arquivo limpo para o Power BI possibilitando a análise e visualização dos dados de pesagem
df.to_csv('pesagens_prontas_powerbi.csv', index=False, sep=';', encoding='utf-8-sig')
