import pandas as pd

vendas_df = pd.read_excel("Vendas.xlsx") #Ler arquivo de excel ja existente / nesse caso o arquivo esta na pasta do curso/ caso estiver em outro lugar, passar o caminho.

#print(vendas_df.describe())

#produtos = vendas_df[['Produto','ID Loja']]
#print(produtos)

#vendas_norteshopping_df = vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping',['ID Loja','Produto','Quantidade']]
#print(vendas_norteshopping_df)

#PEGAR UM VALOR ESPECIFICO
#print(vendas_df.loc[1,'Produto'])

#ADICIONANDO COLUNAS  NOVAS DEPENDENDO DE OUTRAS COLUNAS.
vendas_df['Comissão'] = vendas_df['Valor Final'] * 0.05
print(vendas_df)

#ADICIONANDO COLUNA COM VALOR PADRÃO
vendas_df.loc[:,"Imposto"] = 0
print(vendas_df)

#ADICIONANDO UM ARQUIVO COM OUTRO.
vendas_dez_df = pd.read_excel("Vendas - Dez.xlsx")
vendas_df = vendas_df.append(vendas_dez_df)
print(vendas_df)

#EXCLUIR LINHAS E COLUNAS
vendas_df = vendas_df.drop("Imposto",axis=1) #AXIS É O EIXO : 0 PARA LINHA E 1 PARA COLUNA  /  NESSE CASO  COMO QUERO EXCLUIR TODA A COLUNA IMPOSTO , axis = 1
print(vendas_df)

vendas_df = vendas_df.drop(0, axis = 0)#NESSE CASO QUERO EXCLUIR A LINHA 0 /  axis= 0
print(vendas_df)

#DELETAR LINHAS E COLUNAS COMPLETAMENTE VAZIAS
vendas_df = vendas_df.dropna(how='all' , axis=1) # NESSE DF NAO TEM VALORES VAZIOS ENTÃO NÃO VAI EXECUTAR NADA. DROPNA = TOTALMENTE VAZIO.
# how='all'  = TODAS      --      AXIS = 1 : COLUNAS    AXIS = 0 : LINHAS


#DELETAR LINHAS QUE POSSUEM PELO MENOS 1 VALOR VAZIO.
vendas_df = vendas_df.dropna()

#PREENCHER CAMPOS VAZIOS. NESSE CASO O CAMPO DE COMISSÃO DE DEZ ESTA VAZIO.
vendas_df['Comissão'] = vendas_df['Comissão'].fillna(vendas_df['Comissão'].mean())
#VAMOS PEGAR O CAMPO COMISSÃO
#QUE VAI RECEBER O NOVO VALOR DE COMISSÃO ' fillna() '
#onde dentro do fillna
# o valor da comissão  vai preencher com o valor médio '.mean()'
print(vendas_df)


#PREENCHE COM O ULTIMO VALOR
vendas_df = vendas_df.ffill() # preenche com o valor acima dele

#VER QUANTAS TRANSAÇÕES CADA  SHOPPING TEVE
transacao_loja = vendas_df['ID Loja'].value_counts()
print(transacao_loja)

#AGRUPAR AS INFORMAÇÕES / tabela inteira
fat_prod = vendas_df.groupby('Produto'). sum()
print(fat_prod)

#AGRUPAR AS INFORMAÇÕES / com campos especificos.
fat_prod = vendas_df[['Produto','Valor Final']].groupby('Produto'). sum()
print(fat_prod)

#ABRINDO UMA NOVA TABELA PARA MESCLAR.
gerentes_df = pd.read_excel("Gerentes.xlsx")
print(gerentes_df)

vendas_df = vendas_df.merge(gerentes_df)
print(vendas_df)