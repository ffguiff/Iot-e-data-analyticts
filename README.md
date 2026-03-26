# Iot-e-data-analyticts
Dados brutos de balanças IoT na indústria farmacêutica costumam vir com ruídos: unidades de medida mistas (g e kg), valores nulos por erro de sensor e falta de padronização. Isso impede uma análise real.

  Desenvolvi um script que automatiza a limpeza e o tratamento desses dados:
    *Filtro de Erros: Remove registros gerados por instabilidade no sensor.
    *Conversor de Unidades: Função personalizada que identifica gramas (g) e converte para quilogramas (kg) automaticamente.
    *Agrupamento (BI): Consolida os dados por Lote e Produto para gerar médias precisas de pesagem.

Tecnologias: Python, Pandas, CSV.
