import pandas as pd

# Carregar a planilha e remover espaços extras nos nomes das colunas
file_path = r'SELECIONE O CAMINHO'
df = pd.read_excel(file_path)
df.columns = df.columns.str.strip()

# Corrigir o formato da coluna 'VALOR'
df['VALOR'] = pd.to_numeric(df['VALOR'].replace('[\$,]', '', regex=True), errors='coerce').fillna(0)

# Total de registros na planilha
total_registros = len(df)

# Total de colaboradores distintos
total_colaboradores = df['FUNCIONÁRIO'].nunique()

# Setores presentes na planilha
setores = df['SETOR'].unique()

# Valor total por setor - Formate em R$ com duas casas decimais
valor_total_por_setor = df.groupby('SETOR')['VALOR'].sum().map('R${:.2f}'.format)

# Top 10 Funcionários mais solicitantes - Formate em R$ com duas casas decimais
top_funcionarios = df.groupby('FUNCIONÁRIO')['VALOR'].sum().nlargest(10).map('R${:.2f}'.format)

# Top 10 destinos mais frequentes
top_destinos = df['DESTINO'].value_counts().head(10)

# Valor total por mês/ano - de jan/2021 até dez/2022 - Formate em R$ com duas casas decimais
df['MES_ANO'] = df['DATA'].dt.to_period('M')
valor_total_por_mes_ano = df.groupby('MES_ANO')['VALOR'].sum().map('R${:.2f}'.format)

# Total de 2021, 2022 e geral
total_2021 = df[df['DATA'].dt.year == 2021]['VALOR'].sum()
total_2022 = df[df['DATA'].dt.year == 2022]['VALOR'].sum()
total_geral = df['VALOR'].sum()

# Adicionar totais ao final do Valor total por mês/ano
valor_total_por_mes_ano.loc['Total 2021'] = f'R${total_2021:.2f}'
valor_total_por_mes_ano.loc['Total 2022'] = f'R${total_2022:.2f}'
valor_total_por_mes_ano.loc['Total Geral'] = f'R${total_geral:.2f}'

# Exibir as informações formatadas
print(f"Total de Registros: {total_registros}")
print(f"Total de Colaboradores Distintos: {total_colaboradores}")
print(f"Setores Presentes: {setores}")
print("\nValor Total por Setor:")
print(valor_total_por_setor)
print("\nTop 10 Funcionários Mais Solicitantes:")
print(top_funcionarios)
print("\nTop 10 Destinos Mais Frequentes:")
print(top_destinos)
print("\nValor Total por Mês/Ano:")
print(valor_total_por_mes_ano)
