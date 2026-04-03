import pandas as pd
 
#carrega o arquivo csv
df = pd.read_csv('balanca.csv')

# remover linhas com erro de leitura
df  = df[df['status_sensor'] != 'erro_leitura']

'''O simbolo != significa que o pandas vai olhar para o status 
e criar um linha de verdadeiro ou falso. se falso será igual a erro.
Quando colocado o filtro df[]estou dizendo para o pandas pegar somente as linhas onde a condição é verdadeira 
Ao colocar do df['status_sensor'] dentro de outro df[] estou dizendo para o pandas salvar a nova tabela.'''

# padronizar para kg
def padronizar_peso(row):
    if row['unidade'] == 'g':
        return row ['peso_lido']/1000
    return row['peso_lido']

df['peso_final_kg'] = df.apply(padronizar_peso, axis = 1)

'''row = linha que será analisada 
quando estiver na linha x e a unidade for g ela será dividida por 1000 para padronizar para kg
apply ira executar a função padronizar_peso para cada linha. axis =1 indica que a função deve ser aplicada na horizontal.
é criada uma coluna nova chamada peso_final_kg para armazenar os valores padronizados.'''

# 3 media de peso por lote

media_lote = df.groupby(['lote_id','produto'])['peso_final_kg'].mean()

print("dados processados para insights:")
print(f" Média de peso por lote:\n{media_lote}")
print(df[['timestamp', 'lote_id', 'peso_final_kg', 'status_sensor']])

'''mean() é uma função do pandas que calcula a média
a variavel media_lote se torna meio que uma matriz onde os dados estão agrupados, ela 
é definida dessa forma porque o groupby cria um objeto de grupo.'''
