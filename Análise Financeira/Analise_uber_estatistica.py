import pandas as pd
from scipy.stats import skew, kurtosis

# Carregar a planilha e remover espaços extras nos nomes das colunas
file_path = r'C:\Users\Livia Shara\Desktop\Gabriel Florêncio\Python\Análise Financeira\uber geral.xlsx'
df = pd.read_excel(file_path)
df.columns = df.columns.str.strip()

# Calcular o coeficiente de variação para a coluna 'VALOR'
coefficient_of_variation = (df['VALOR'].std() / df['VALOR'].mean()) * 100

# Carregar a planilha e remover espaços extras nos nomes das colunas
file_path = r'C:\Users\Livia Shara\Desktop\Gabriel Florêncio\Python\Análise Financeira\uber geral.xlsx'
df = pd.read_excel(file_path)
df.columns = df.columns.str.strip()

# Calcular estatísticas descritivas para a coluna 'VALOR'
estatisticas_descritivas = df['VALOR'].describe()

# Calcular a moda
moda = df['VALOR'].mode().iloc[0]

# Calcular a variância
variancia = df['VALOR'].var()

# Calcular a assimetria e curtose
assimetria = skew(df['VALOR'])
curtose = kurtosis(df['VALOR'])

# Exibir os resultados
print("Estatísticas Descritivas para a coluna 'VALOR':")
print(estatisticas_descritivas)

print(f"Coeficiente de Variação para a coluna 'VALOR': {coefficient_of_variation:.2f}%")
print(f"\nModa para a coluna 'VALOR': {moda}")
print(f"Variância para a coluna 'VALOR': {variancia:.2f}")
print(f"Assimetria para a coluna 'VALOR': {assimetria:.2f}")
print(f"Curtose para a coluna 'VALOR': {curtose:.2f}")
