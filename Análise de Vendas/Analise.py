import pandas as pd

# Carregar a planilha
caminho_arquivo = r'SELECIONE O CAMINHO DESEJADO'
df = pd.read_excel(caminho_arquivo)

# Remover caracteres especiais
df = df.applymap(lambda x: x.encode('unicode_escape').decode('utf-8') if isinstance(x, str) else x)

# Converter colunas numéricas para formato monetário (R$)
colunas_monetarias = ['Total_Vendas', 'Desconto', 'Valor Bruto', 'Valor Líquido']
df[colunas_monetarias] = df[colunas_monetarias].apply(lambda x: 'R${:.2f}'.format(x) if isinstance(x, (int, float)) else x)

# Análise Estatística Descritiva
analise_descritiva = df.describe(include='all')

# Imprimir análise estatística descritiva
print("\nAnálise Estatística Descritiva:")
print(analise_descritiva)

# Valor líquido por país
valor_liquido_por_pais = df.groupby('Pais')['Valor Líquido'].sum()
print("\nValor Líquido por País:")
print(valor_liquido_por_pais)

# Valor líquido por segmento
valor_liquido_por_segmento = df.groupby('Segmento')['Valor Líquido'].sum()
print("\nValor Líquido por Segmento:")
print(valor_liquido_por_segmento)

# Média de vendas por país
media_vendas_por_pais = df.groupby('Pais')['Total_Vendas'].mean()
print("\nMédia de Vendas por País:")
print(media_vendas_por_pais)

# Quantidade total de vendas por categoria
quantidade_vendas_por_categoria = df.groupby('Categoria')['Quantidade'].sum()
print("\nQuantidade Total de Vendas por Categoria:")
print(quantidade_vendas_por_categoria)

# Valor médio de desconto por segmento
valor_medio_desconto_por_segmento = df.groupby('Segmento')['Desconto'].mean()
print("\nValor Médio de Desconto por Segmento:")
print(valor_medio_desconto_por_segmento)

# Outras análises específicas podem ser adicionadas conforme necessário

# Salvando a planilha modificada
df.to_excel(r'SELECIONE O CAMINHO', index=False)

print("\nAnálise completa realizada e planilha formatada salva com sucesso.")
